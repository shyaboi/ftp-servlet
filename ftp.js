const ftp = require("basic-ftp")
const dotenv = require('dotenv');
dotenv.config();

//TODO make new copy of file
// const fs = require('fs')

// try {
//   const data = fs.readFileSync('/Users/joe/test.txt', 'utf8')
//   console.log(data)
// } catch (err) {
//   console.error(err)
// }
download()

async function download() {
    const client = new ftp.Client()
    client.ftp.verbose = true
    try {
        await client.access({
            host: process.env.HOST,
            user: process.env.USER,
            password: process.env.PASS,
            secure: true
        })
        console.log(await client.list())
        // await client.uploadFrom("README.md", "README_FTP.md")
        await client.downloadToDir('./testFiles', "/www")
    }
    catch(err) {
        console.log(err)
    }
    client.close()
}