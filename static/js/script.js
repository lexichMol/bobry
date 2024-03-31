

async function getRooms () {
    let formData = new FormData();
    let _arr = document.getElementById("arrive_date").value;
    formData.append("arr", _arr);
     let response = await fetch("http://192.168.0.141:5000/api/v1.0/show_rooms",
            {
                method: "POST",
                body: formData
            });
     let result = await response.json();
}


document.getElementById("show_rooms_btn").addEventListener("click", async () => {
    let v = document.getElementById("date-select").value;
    document.getElementById("date_part").innerHTML = v;
    let formData = new FormData();
    formData.append("date", v);
    let response = await fetch("http://192.168.0.141:5000/api/v1.0/show_rooms",
            {
                method: "POST",
                body: formData
            });
     let result = await response.json();
    document.getElementById("rooms_block").innerHTML = "";
     document.getElementById("text_span_upper1").innerHTML = result["rooms_count"];
     document.getElementById("text_span_upper2").innerHTML = result["window_on_floor"];


     document.getElementById("text_span_upper3").innerHTML = result["k"];
     document.getElementById("text_span_upper4").innerHTML = result["rooms_with_light"];


    let all_windows = result["all_windows"].split(";").reverse();
    console.log(all_windows);




     let floor_count = result["floors_count"];


    let cell = document.createElement("div");
    cell.setAttribute("class", "room");


    let field_row = document.createElement("div");
    field_row.setAttribute("class", "field_row");
     for (let i = 0; i < floor_count; i++) {
        let new_row = field_row.cloneNode();
        new_row.setAttribute("id", String(i));

        let about_rooms = all_windows[i].split(",");
        console.log(about_rooms);

        for (let j = 0; j < about_rooms.length; j++) {
            let new_room = cell.cloneNode();
            let current_room = about_rooms[j].split(" ");
            if (current_room[0] == "True") {
                 new_room.setAttribute("class", "light_room");
            } else {
                 new_room.setAttribute("class", "black_room");
            }
            new_room.innerHTML = current_room[1];
            new_row.appendChild(new_room);
        }

        document.getElementById("rooms_block").appendChild(new_row);

     }





     console.log(result["floors_count"]);

})


// N = parseInt(N);
//
//    let field_row = document.createElement("div");
//    field_row.setAttribute("class", "field_row");
//
//    let cell = document.createElement("div");
//    cell.setAttribute("class", "cell");
//    field_html.style.display = "flex";
//
//
//    for (let i = 0; i < N; i++) {
//        field.push(new Array(N));
//        let new_row = field_row.cloneNode();
//        new_row.setAttribute("id", String(i));
//
//