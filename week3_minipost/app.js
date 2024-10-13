const express = require('express')
const app = express()

const mongoose =require('mongoose')
require('dotenv/config') // imports .env environment variables

const bodyParser = require('body-parser')
const postsRoute = require('./routes/posts')

app.use(bodyParser.json())
app.use('/posts',postsRoute)

app.get('/', (req,res) =>{
    res.send('Homepage')
})

mongoose.connect(process.env.DB_CONNECTOR).then(()=>{
    console.log('DB is working')
})

app.listen(3000, ()=>{
    console.log('Server is up and running...')
})