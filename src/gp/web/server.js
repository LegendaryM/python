const express = require('express');
const fs = require('fs');
const path = require('path');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;
const imagesDir = 'E:/1gp/png';

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/', (req, res) => {
  const paihang = fs.readFileSync(path.join(imagesDir, `paihang.txt`), 'utf8').trim();
  const ph_details = JSON.parse(paihang);

  const ph_details_all = ph_details.map(ph_detail => {
    const f12 = ph_detail.f12
    const statusFile = path.join(imagesDir, `${f12}.txt`);
    let status = '';
    if (fs.existsSync(statusFile)) {
        status = fs.readFileSync(statusFile, 'utf8').trim();
    }

    let f62 = ph_detail.f62;
    if (f62 >= 100000000) { // 1亿
      f62 = (f62 / 100000000).toFixed(2) + '亿';
    } else if (f62 >= 10000) {
      f62 = (f62 / 10000).toFixed(2) + '万';
    }  else if (f62 <= -100000000) {
      f62 = (f62 / 100000000).toFixed(2) + '亿';
    } else if (f62 <= -10000) {
      f62 = (f62 / 10000).toFixed(2) + '万';
    } else {
    }
    return { name: ph_detail.f14 + "_" + ph_detail.f12 + " -> " + f62, code:f12, status};
  })

  res.render('index', { images: ph_details_all });
});

app.post('/setStatus', (req, res) => {
  const parent = req.body.parent;
  const code = req.body.code;
  const value = req.body.value;
  let final_path = path.join(imagesDir, code + '.txt')
  if (parent != '') {
    final_path = path.join(imagesDir, parent + "_details", code + '.txt')
  }
  fs.writeFile(final_path, value , (err) => {
    if (err) {
      return res.status(500).send('Unable to write file: ' + err);
    }
    res.send('Image name written to file successfully');
  });
});

app.get('/t', (req, res) => {
  const code = req.query.code;
  if (!fs.existsSync(path.join(imagesDir, code + '_details', `paihang.txt`))) {
    res.send({ images: [], name: '', code })
    return;
  }
  const paihang = fs.readFileSync(path.join(imagesDir, code + '_details', `paihang.txt`), 'utf8').trim();

  const splits = paihang.split('\n')
  const name = splits[0]
  const ph_details = JSON.parse(splits[1]);

  const ph_details_all = ph_details.map(ph_detail => {
    const f12 = ph_detail.f12
    const statusFile = path.join(imagesDir, code + '_details', `${f12}.txt`);
    let status = '';
    if (fs.existsSync(statusFile)) {
        status = fs.readFileSync(statusFile, 'utf8').trim();
    }

    let f62 = ph_detail.f62;
    if (f62 >= 100000000) { // 1亿
      f62 = (f62 / 100000000).toFixed(2) + '亿';
    } else if (f62 >= 10000) {
      f62 = (f62 / 10000).toFixed(2) + '万';
    }  else if (f62 <= -100000000) {
      f62 = (f62 / 100000000).toFixed(2) + '亿';
    } else if (f62 <= -10000) {
      f62 = (f62 / 10000).toFixed(2) + '万';
    } else {
    }
    return { name: ph_detail.f14 + "_" + ph_detail.f12 + " -> " + ph_detail.f3 + "%_" + f62, code:f12, status};
  })

  res.send({ images: ph_details_all, name,code })
});


app.use('/images', express.static(imagesDir));

const os = require('os');

// 获取网络接口信息
const networkInterfaces = os.networkInterfaces();

// 遍历所有网络接口
for (const interfaceName in networkInterfaces) {
    const addresses = networkInterfaces[interfaceName];
    for (const addressInfo of addresses) {
        // 检查IPv4地址并且不是内部地址（例如127.0.0.1）
        if (addressInfo.family === 'IPv4' && !addressInfo.internal) {
            console.log(`IP Address: ${addressInfo.address}`);
        }
    }
}

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
