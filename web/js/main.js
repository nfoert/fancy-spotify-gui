var url = ""

async function get_song_data() {
    // Inside a function marked 'async' we can use the 'await' keyword.

    let n = await eel.get_song_data()(); // Must prefix call with 'await', otherwise it's the same syntax

    if (url != n["url"]) {
        console.log("Theres a new song!")
        document.getElementById("art").classList.add("element-appears");

        setTimeout(function() {
            document.getElementById("art").src = n["cover_art"];
            document.getElementById("background").src = n["cover_art"]
        }, 250);

        setTimeout(function() {
            document.getElementById("art").classList.remove("element-appears");
        }, 500);


        // There's a new song!
        null;
    }

    

    document.getElementById("title").innerText = n["title"]
    document.getElementById("artist").innerText = n["artist"]
    document.getElementById("album").innerText = n["album"]

    url = n["url"];

}

setInterval(get_song_data, 1000);