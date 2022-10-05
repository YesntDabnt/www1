function changeThing(){
    let displayImage = document.getElementById('image2')
    if(displayImage.src.match('https://www.freeiconspng.com/thumbs/pokeball-png/pokeball-icon-download-23.png')){
        displayImage.src = '/övningar/openball.png'
    }   
    else{
        displayImage.src = 'https://www.freeiconspng.com/thumbs/pokeball-png/pokeball-icon-download-23.png'
    }
     
    }