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

// request specific feedback from user
router.get('/:filmID', async(req,res)=>{
    try{
        const filmByID = await Film.findById(req.params.filmID)
        res.send(filmByID)
    }catch(err){
        res.send({message:err})
    }
})


module.exports = router