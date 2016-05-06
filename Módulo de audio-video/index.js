$(function () {


    var pButton = $("#pButton");
    var music = $("#music")[0];
    var mNextButton = $("#nextButton");
    var mPreviousButton = $("#previousButton");

    var mTimeline = $("#timeline");

    var mPlayedAudio = $("#played-audio");
    var mUnplayedAudio = $("#unplayed-audio");
    var mSongPlayinLabel = $("#song-playing");

    var mDuration;


    var input = $("#input-name");
    var send = $("#send");
    var mExit = $("#exit");


    var mPeopleList = $("#people-list");


    var mImages = ["elton_john.jpg", "what_went_down.jpg", "in_rainbows.jpg"];


    var david = {
        "persona": {
            "nombre": "David Azar",
            "audio": [{
                "nombre": "London Thunder",
                "album": "What Went Down",
                "src": "http://localhost:8000/static/audio/London_Thunder.mp3",
                "artista": "Foals",
                "imagen": "http://localhost:8000/static/imagenes/what_went_down.jpg"
            },
                {
                    "nombre": "15 Step",
                    "album": "In Rainbows",
                    "src": "http://localhost:8000/static/audio/15_Step.mp3",
                    "artista": "Radiohead",
                    "imagen": "http://localhost:8000/static/imagenes/in_rainbows.jpg"
                }],
            "img": [
                "http://localhost:8000/static/imagenes/david_1.jpg",
                "http://localhost:8000/static/imagenes/david_2.jpg"
            ]
        },
        "accion": "in"
    };


    var daniel = {
        "persona": {
            "nombre": "Daniel Castro",
            "audio": [{
                "nombre": "Sun In Your Eyes",
                "album": "Shields",
                "src": "http://localhost:8000/static/audio/Sun_In_Your_Eyes.mp3",
                "artista": "Grizzly Bear",
                "imagen": "http://localhost:8000/static/imagenes/shields.jpg"
            },
                {
                    "nombre": "Time",
                    "album": "Dark Side Of The Moon",
                    "src": "http://localhost:8000/static/audio/time.mp3",
                    "artista": "Pink Floyd",
                    "imagen": "http://localhost:8000/static/imagenes/dark_side_of_the_moon.png"
                }],
            "img": [
                "http://localhost:8000/static/imagenes/daniel_1.jpg",
                "http://localhost:8000/static/imagenes/daniel_2.jpg"
            ]
        },
        "accion": "in"
    };


    var mAllImages = [];

    //var allSongs = [song, song2, song3, song4];


    var mCarousel = $("#carousel-inner-container");


    var mQueue = $("#queue");
    var mCurrentSong = 0;
    var mAudioQueue = [];




    //setInterval(1000);

    function addSongsToQueue(songs) {

        if (mAudioQueue.length === 0) {
            mAudioQueue = songs;
            return;
        }


        var temporalQueue = mAudioQueue;
        mQueue.empty();

    }

    send.click(function (event) {

        var name = input.val();
        var person;

        switch (name) {

            case 'David':
                person = david;
                break;

            case 'Daniel':
                person = daniel;
                break;


            case 'Charly':
                person;
                break;


        }

        personEnter(person);


    });


    function personEnter(person) {

        var name = person.persona.nombre;

        var html = '<li class="person"><p class="person-name">' + name + '</p></li>';
        $(html).hide().appendTo(mPeopleList).fadeIn(400);

        var songs = person.persona.audio;
        var queue = getJointSongs(songs);

        addSongs(queue);


        var images = getPersonImages(person);
        var imageQueue = getJointImages(images);
        addImagesToCarousel(imageQueue);
        //addSongsToQueue(songs);
    }


    function personExit(person) {

        var songs = $(".song-title");

        console.log("VALOR: " + $(songs.eq(0)).text());


        mSongPlayinLabel.text("___");
        var userAudio = person.persona.audio;

        var index;
        for (var i = 0; i < userAudio.length; i++) {

            index = findSongIndex(userAudio[i].nombre, songs);


            var songToDelete = $(".song").eq(index);
            songToDelete.fadeOut(400, function () {
                $(this).remove();
            });

        }

        var listItems = $("ul#people-list li");
        index = getNameToRemove(listItems, person.persona.nombre);
        var itemToDelete = $(".person").eq(index);

        itemToDelete.fadeOut(400, function () {
            $(this).remove();
        });


        removePersonAudio(person);

        removePersonImages(person);

        mCarousel.empty();
        addImagesToCarousel(mAllImages);

    }


    function removePersonAudio(person) {

        var names = getSongNamesByPerson(person);

        var size = mAudioQueue.length;
        //for (var i = 0; i < size; i++) {
        //
        //    if (mAudioQueue.length === 0) break;
        //
        //    //console.log("BOrrando: " + mAudioQueue[i].nombre);
        //
        //    var songName = mAudioQueue[i].nombre;
        //
        //    for (var j = 0; j < names.length; j++) {
        //
        //        if (songName === names[j]) {
        //            mAudioQueue.splice(i, 1);
        //            i--;
        //        }
        //
        //
        //    }
        //
        //
        //}





        for ( var i = 0; i<names.length; i++){


            for(var j = 0; j<mAudioQueue.length;j++){

                if(mAudioQueue[j].nombre === names[i]){
                    mAudioQueue.splice(j,1);
                    break;
                }

            }

        }


        //var i = 0;
        //while (i < size) {
        //
        //    if(mAudioQueue.length === 0)break;
        //
        //    var songName = mAudioQueue[i].nombre;
        //    //var songName = mAudioQueue[0].nombre;
        //
        //    for (var j = 0; j < names.length; j++) {
        //
        //        if (songName === names[j]) {
        //
        //            //var indexToRemove = findSongIndexInQueue(mAudioQueue[0]);
        //
        //            mAudioQueue.splice(i, 1);
        //            i--;
        //            //break;
        //        }
        //        //else {
        //        //    i++;
        //        //}
        //
        //
        //    }
        //
        //    i++;
        //
        //
        //}




    }


    function removePersonImages(person) {


        var images = getPersonImages(person);

        var size = mAllImages.length;


        var imagesInCarousel = $(".imagen-carousel");


        //for (var i = 0; i < size; i++) {
        //
        //    if (mAllImages.length === 0) break;
        //
        //    var img = imagesInCarousel.find("img").eq(i);
        //    var src = img.attr("src");
        //
        //    for (var j = 0; j < images.length; j++) {
        //
        //        if (src === images[j]) {
        //            mAllImages.splice(i, 1);
        //            i--;
        //        }
        //    }
        //}
        //


        for(var i = 0;i<images.length;i++){


            for(var j =0; j<mAllImages.length; j++){

                if(mAllImages[j] === images[i]){
                    mAllImages.splice(j,1);
                    break;
                }
            }


        }


        //var i = 0;
        //while (i < size) {
        //
        //
        //    //var img = imagesInCarousel.find("img").eq(i);
        //    var img = imagesInCarousel.find("img").eq(i);
        //    var src = img.attr("src");
        //
        //    for (var j = 0; j < images.length; j++) {
        //
        //        if (src === images[j]) {
        //            var indexToRemove = findImageIndex(src);
        //            mAllImages.splice(indexToRemove, 1);
        //            //i--;
        //            //break;
        //        }
        //        //else {
        //        //    i++;
        //        //}
        //    }
        //    i++;
        //
        //}
    }


    function findImageIndex(image){

        var index = 0;

        for(var i = 0; i<mAllImages.length; i++){

            if(image === mAllImages[i]){
                index = i;
            }

        }

        return index;

    }


    function findSongIndexInQueue(song){


        var index = 0;

        for(var i = 0;i<mAudioQueue.length;i++){

            if(song.nombre === mAudioQueue[i].nombre){
                index = i;
            }
        }

        return index;
    }

    function getSongNamesByPerson(person) {


        var names = [];

        for (var i = 0; i < person.persona.audio.length; i++) {
            names.push(person.persona.audio[i].nombre);
        }

        return names;


    }


    function getJointSongs(songs) {


        if (mAudioQueue.length === 0) {
            for (var i = 0; i < songs.length; i++) {
                mAudioQueue.push(songs[i]);
            }


            music.src = mAudioQueue[0].src;

            return mAudioQueue;
        }

        var temporalQueue = mAudioQueue;

        mQueue.empty();


        for (var i = 0; i < songs.length; i++) {
            temporalQueue.push(songs[i]);
        }

        mAudioQueue = shuffle(temporalQueue);

        return mAudioQueue;

    }


    function getJointImages(images) {


        if (mAllImages.length === 0) {
            for (var i = 0; i < images.length; i++) {
                mAllImages.push(images[i]);
            }

            return mAllImages;
        }

        var temporalImages = mAllImages;

        mCarousel.empty();

        for (var i = 0; i < images.length; i++) {
            temporalImages.push(images[i]);
        }

        mAllImages = shuffle(temporalImages);
        return mAllImages;

    }


    mExit.click(function (event) {

        var name = input.val();
        //
        //var listItems = $("ul#people-list li");
        //console.log("Size: " + listItems.length);
        //
        //var index = getNameToRemove(listItems, name);
        //
        //console.log("Voy a borrar al: " + index);
        //
        ////var itemToDelete = listItems[index];
        //
        //
        ////var itemToDelete = $("ul#people-list li:nth-child(0)");
        //
        //
        //var itemToDelete = $(".person").eq(index);
        //
        //itemToDelete.fadeOut(400, function () {
        //    $(this).remove();
        //});
        //
        //
        //console.log(itemToDelete);


        var person;
        switch (name) {

            case 'David':
                person = david;
                break;

            case 'Daniel':
                person = daniel;
                break;


            case 'Charly':
                person;
                break;


        }


        personExit(person);


    });


    //mTimeline.click(function (event) {
    //
    //    var percentage = timelineClickPercentage(event, this);
    //
    //    mPlayedAudio.css("width", percentage * 100 + "%");
    //    mUnplayedAudio.css("width", (100 - percentage * 100) + "%");
    //
    //    var newPosition = mDuration * percentage;
    //    console.log("Music duration check: " + music.duration);
    //    console.log("Update currentTime: " + newPosition);
    //    music.currentTime = newPosition;
    //
    //
    //    //music.play();
    //
    //});


    //music.src = "audio/Sun_In_Your_Eyes.mp3";


    music.addEventListener("canplaythrough", function () {

        console.log("Can play through");
        mDuration = music.duration;
    }, false);


    music.addEventListener('timeupdate', function () {

        var percentage = 100 * (music.currentTime / mDuration);

        mPlayedAudio.css("width", percentage + "%");
        mUnplayedAudio.css("width", (100 - percentage) + "%");

    }, false);


    function timelineClickPercentage(event, timeline) {

        console.log("CLICK TIMELINE");

        var percentage = (event.pageX - $(timeline).offset().left) / $(timeline).width();
        console.log("Porcentaje:  " + percentage);

        return percentage;
    }


    function getNameToRemove(list, nameToDelete) {


        var finalIndex;

        list.each(function (index) {


            var paragraph = $(this).find("p.person-name");

            var displayedName = paragraph.text();

            if (nameToDelete === displayedName) {
                finalIndex = index;
                this.break;
            }

        });

        return finalIndex;

    }


    function addImagesToCarousel(images) {

        for (var i = 0; i < images.length; i++) {

            if (i === 0) {
                var html = '<div class="item imagen-carousel active"><img class="img-responsive center-block" src=' + images[i] + '></div>';
            }
            else {
                var html = '<div class="item imagen-carousel"><img class="img-responsive center-block" src=' + images[i] + '></div>';
            }
            mCarousel.append(html);
        }


    }

    function getPersonImages(person) {

        var images = [];

        for (var i = 0; i < person.persona.img.length; i++) {

            images.push(person.persona.img[i]);

        }

        return images;


    }

    function findSongIndex(song, list) {

        var songIndex;

        list.each(function (index) {

            if (song === list.eq(index).text()) {
                songIndex = index;
                this.break;
            }
        });

        return songIndex;


    }


    pButton.click(function (event) {

        console.log("Click a play");


        if (music.paused) {

            music.play();
            mSongPlayinLabel.text(mAudioQueue[mCurrentSong].nombre);

            console.log("SONG NAME: " + mAudioQueue[mCurrentSong].nombre);
            this.className = "";
            this.className = "pause";

        } else {

            music.pause();
            this.className = "";
            this.className = "play";

        }

    });

    mNextButton.click(function (event) {

        if (mCurrentSong >= 0 && mCurrentSong < mAudioQueue.length - 1)
            mCurrentSong++;

        music.src = mAudioQueue[mCurrentSong].src;
        mSongPlayinLabel.text(mAudioQueue[mCurrentSong].nombre);
        music.pause();
        music.load();
        music.play();


        if (pButton.className === "play") {
            pButton.className = "";
            pButton.className = "pause";
        }


    });


    mPreviousButton.click(function (event) {

        if (mCurrentSong > 0 && mCurrentSong < mAudioQueue.length)
            mCurrentSong--;

        music.src = mAudioQueue[mCurrentSong].src;
        mSongPlayinLabel.text(mAudioQueue[mCurrentSong].nombre);
        music.pause();
        music.load();
        music.play();

    });

    music.addEventListener('ended', function () {

        if (mCurrentSong >= 0 && mCurrentSong < mAudioQueue.length - 1) {
            mCurrentSong++;
            music.src = mAudioQueue[mCurrentSong].src;
            mSongPlayinLabel.text(mAudioQueue[mCurrentSong].nombre);
            music.pause();
            music.load();
            music.play();
        }

        else {
            music.pause();
            mCurrentSong = 0;
            music.src = mAudioQueue[0].src;
        }

    });

    music.addEventListener('play', function () {


        console.log("PLAYYYY");
        pButton.removeClass();
        pButton.addClass("pause");

        mSongPlayinLabel.text(mAudioQueue[mCurrentSong].nombre);

    });

    music.addEventListener('pause', function () {


        console.log("PAUSEEEE");
        pButton.removeClass();
        pButton.addClass("play");


    });


    function addSongs(songs) {

        for (var i = 0; i < songs.length; i++) {

            var html = '<li class="song">' +
                '<img class="artwork" src=' + songs[i].imagen + '>' +
                '<div class="song-metadata">' +
                '<p class="song-title">' + songs[i].nombre + '</p>' +
                '<p class="song-artist">' + songs[i].artista + '</p>' +
                '<p class="song-album">' + songs[i].album + '</p>' +
                '</div>' +
                '</li>';


            $(html).hide().appendTo(mQueue).fadeIn(400);


        }


    }


    function shuffle(array) {
        var currentIndex = array.length, temporaryValue, randomIndex;

        // While there remain elements to shuffle...
        while (0 !== currentIndex) {

            // Pick a remaining element...
            randomIndex = Math.floor(Math.random() * currentIndex);
            currentIndex -= 1;

            // And swap it with the current element.
            temporaryValue = array[currentIndex];
            array[currentIndex] = array[randomIndex];
            array[randomIndex] = temporaryValue;
        }

        return array;
    }




    setInterval(function () {
        data = {hello: 'hello'};
        console.log('TIME');
        $.get( "http://192.168.1.200:8000/home/pipeline/",data, function (data){
            console.log('SUCCESS');
            console.log(data);


            console.log("DATOS___action "+data.accion);


            var action = data.accion;
            if(action === "in")
            personEnter(data);

            else if(action === "out")
            personExit(data);




        });
    }, 3000);




});

