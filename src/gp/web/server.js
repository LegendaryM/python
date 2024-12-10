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
  const hangye = fs.readFileSync(path.join(imagesDir, `paihang.txt`), 'utf8').trim();
  const hangye_json = JSON.parse(hangye);

  const hangye_details = hangye_json.map(hangye => {
    const f12 = hangye.f12
    const statusFile = path.join(imagesDir, `${f12}.txt`);
    let status = '';
    if (fs.existsSync(statusFile)) {
        status = fs.readFileSync(statusFile, 'utf8').trim();
    }

    v = huansuan(hangye.f62)
    const f62 = v[0]
    const color_zj = v[1]
    return { name: hangye.f14 + "_" + hangye.f12 + " -> " + f62, code:f12, status,'color_zj':color_zj, 'color_zf':''};
  })

  const hangye_details_all = hangye_details.map(hangye => {
    gegus = []
    const code = hangye.code;
    paihang_txt = path.join(imagesDir, code + '_details', `paihang.txt`)
    if (!fs.existsSync(paihang_txt)) {
      gegus = []
    } else {
      const paihang = fs.readFileSync(paihang_txt, 'utf8').trim();
      const gegu_details = JSON.parse(paihang);
  
      gegus = gegu_details.map(gegu => {
        const f12 = gegu.f12
        const statusFile = path.join(imagesDir, code + '_details', `${f12}.txt`);
        let status = '';
        if (fs.existsSync(statusFile)) {
            status = fs.readFileSync(statusFile, 'utf8').trim();
        }
  
        v = huansuan(gegu.f62)
        const f62 = v[0]
        const color_zj = v[1] // 资金

        let color_zf = 'red'  // 涨幅
        if (gegu.f3 < 0) {
          color_zf = 'green'
        }
        return { name: gegu.f14 + "_" + gegu.f12 + " -> ", 'f3':gegu.f3, 'f62':f62, code:f12, status, 'color_zj':color_zj, 'color_zf':color_zf};
      })
    }
    hangye['gegus'] = gegus
    hangye['gegus_length'] = gegus.length
    return hangye;
  })
    
  res.render('index', { images: hangye_details_all });
});


function huansuan(f62) {
  let color = 'red'
  let f62_ = f62
  if (f62 >= 100000000) { // 1亿
    f62_ = (f62 / 100000000).toFixed(2) + '亿';
  } else if (f62 >= 10000) {
    f62_ = (f62 / 10000).toFixed(2) + '万';
  }  else if (f62 <= -100000000) {
    f62_ = (f62 / 100000000).toFixed(2) + '亿';
    color = 'green'
  } else if (f62 <= -10000) {
    f62_ = (f62 / 10000).toFixed(2) + '万';
    color = 'green'
  } else {
  }
  return [f62_, color]
}


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

app.get('/show_summary', (req, res) => {
  const hangye = fs.readFileSync(path.join(imagesDir, `paihang.txt`), 'utf8').trim();
  const hangye_json = JSON.parse(hangye);

  const hangye_details = hangye_json.map(hangye => {
    const f12 = hangye.f12
    const statusFile = path.join(imagesDir, `${f12}.txt`);
    let status = '';
    if (fs.existsSync(statusFile)) {
        status = fs.readFileSync(statusFile, 'utf8').trim();
    }

    v = huansuan(hangye.f62)
    const f62 = v[0]
    return { name: hangye.f14 + "_" + hangye.f12 + " -> " + f62, code:f12, status};
  })

  const hangye_details_all = hangye_details.map(hangye => {
    gegus = []
    const code = hangye.code;
    paihang_txt = path.join(imagesDir, code + '_details', `paihang.txt`)
    if (!fs.existsSync(paihang_txt)) {
      gegus = []
    } else {
      const paihang = fs.readFileSync(paihang_txt, 'utf8').trim();
      const gegu_details = JSON.parse(paihang);
      
      gegus = gegu_details.map(gegu => {
        let has_remark=0
        const f12 = gegu.f12
        const statusFile = path.join(imagesDir, code + '_details', `${f12}.txt`);
        let status = '';
        if (fs.existsSync(statusFile)) {
            status = fs.readFileSync(statusFile, 'utf8').trim();
            has_remark = 1
        }
  
        v = huansuan(gegu.f62)
        const f62 = v[0]
        const color_zj = v[1] // 资金

        return { name: gegu.f14 + "_" + gegu.f12 + " -> ", 'f3':gegu.f3, 'f62':f62, code:f12, status, has_remark};
      })
    }
    hangye['gegus'] = gegus
    hangye['gegus_length'] = gegus.length
    return hangye;
  })
    
  res.render('index1', { images: hangye_details_all });
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
