const express = require('express')
const router = express.Router()

const Film = require('../models/Film')

router.get('/', async (req, res)=>{
    try{
        const films = await Film.find() // .limit(5)
        res.send(films)
    }catch(err){
        res.sent({message:err})
    }
})

module.exports = router