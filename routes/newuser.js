// will contain all the user related routes
const express = require('express')
const mysql = require('mysql')
const router = express.Router()


router.get('/messages', (req, res) => {
  console.log("11111111")
  res.end()
})

router.get("/users", (req, res) => {
    const connection = getConnection()
    const queryString = "SELECT * FROM entry"
    connection.query(queryString, (err, rows, fields) => {
      if (err) {
        console.log("The error is:" + err)
        res.sendStatus(500)
        return
      }
      res.json(rows)
    })
  })

const pool = mysql.createPool({
    connectionLimit: 10,
    host: 'localhost', 
    user: 'root', 
    password: 'password', 
    database: 'TrackDB'
})

function getConnection() {
    return pool
}

router.post('/user_create', (req, res) => {
    console.log("Trying to create a new user...")
    console.log("How do we get the form data???")
  
    console.log("First name: " + req.body.create_first_name)
    const Name = req.body.create_user
    
  
    const queryString = "INSERT INTO entry (Name) VALUES (?, ?)"
    getConnection().query(queryString, [firstName, lastName], (err, results, fields) => {
      if (err) {
        console.log("Failed to insert new user: " + err)
        res.sendStatus(500)
        return
      }
  
      console.log("Inserted a new user with id: ", results.insertId);
      res.end()
    })
  })
  
  // fetch info using routes 
router.get('/user/:Name', (req, res) => {
    console.log("Fetching user with name: " + req.params.Name)

    const connection = getConnection()

    const userName = req.params.Name
    const queryString = "SELECT * FROM entry WHERE Name = ?"
    connection.query(queryString, [userName], (err, rows, fields) => {
        if (err) {
        console.log("failed, the error is :  " + err)
        res.sendStatus(500)
        return
        // throw err
        }

        console.log("we were successfull ")

        const users = rows.map((row) => {
        return {name: row.Name, event: row.event_id, grade: row.Grade, mark: row.Mark}
        })

        res.json(users)
    })
})
//root to /user/id
router.get('/user/:event_id',(req, res) => {
    console.log ("getting athlete using their id :" +req.params.event_id)
    
    const connection = getConnection()

    const ath_id  = req.params.event_id
    const queryString = "SELECT * FROM trackdatatest WHERE event_id = ? "
    connection.query(queryString,[ath_id], (err, rows,fields) =>{
        if(err){
            console.log("this error has occured:" + err)
            return res.sendStatus(500)
            
        }
        console.log("athletes selected successfully.. let's see")

        const users= rows.map((row) => {
            return {name: row.Name, meet: row.Meet}

        })
        res.json(users)
    })
    
})

module.exports = router