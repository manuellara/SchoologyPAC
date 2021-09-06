const puppeteer = require('puppeteer');
require('dotenv').config();


(async () => {
    const browser = await puppeteer.launch({ 
      // headless: false
      headless: true,
      args: [
          "--disable-gpu",
          "--disable-dev-shm-usage",
          "--disable-setuid-sandbox",
          "--no-sandbox",
      ]
    });

    const page = await browser.newPage();

    await page.setDefaultNavigationTimeout(0);

    // navigation action
    await page.goto('https://app.schoology.com/');

    // login action
    await page.type('#edit-mail', process.env.USR);
    await page.type('#edit-pass', process.env.PWD);
    await page.type('#edit-school', process.env.SD);

    await page.waitForTimeout('3000');

    await page.keyboard.press('Enter');

    await Promise.all([
      page.waitForNavigation('networkidle0'),
      page.click('#edit-submit'),
    ]);

    // after login, go straight to User Management > Parents/Advisors > Download All (Download Parent Access Codes), select 'Student' and download zip file
    await page.goto('https://app.schoology.com/enrollment/code/paccexport/school/2597647331');

    // change default download location
    await page._client.send('Page.setDownloadBehavior', {behavior: 'allow', downloadPath: './downloads'});

    await page.select('#pacc-role', '771619');

    await page.click('.submit-btn');

    // wait 10 sec
    await page.waitForTimeout('10000');

    // take screenshot
    // await page.screenshot({ path: 'example.png' });
  
    // close browser
    await browser.close();
  })();