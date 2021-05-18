const express = require('express')
const web = express()
const mysql = require ('mysql')
const morgan = require('morgan'); 
const bodyParser = require('body-parser');

web.use(bodyParser.urlencoded({extended: false})) // helps running the request easier. 



web.use(express.static('./htmlcontent')) // access html content

web.use(morgan('short')) // http request logger middelware

const router = require('./routes/newuser.js')   //connect 

web.use(router)

web.get("/", (req, res) =>{
    console.log("we are getting a response from route")
    res.send("hello World")


})
//localhost is 3000
web.listen(3000, () =>{
    console.log('server is running on port 3000')
});   