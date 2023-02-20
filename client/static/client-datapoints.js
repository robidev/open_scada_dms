function init_dataproviders(){

    socket.on('update_dataprovider_status', function (json) {
      table.getRows().forEach((row_element) => {
        if(row_element.getData().dataprovider == json.dataprovider){
          row_element.getData().online = json.online;
        }
      });
    });

    function refresh_dataproviders_table(){
      socket.emit('get_dataproviders',{},function(result){
        //console.log(result);
        table.replaceData(result);
      });
    }

    var table = new Tabulator("#mmi_svg", {
      autoColumns:true, //create columns from data field names
      //data:tabledata,           //load row data from array
      layout:"fitColumns",      //fit columns to width of table
      responsiveLayout:"hide",  //hide columns that dont fit on the table
      //tooltips:true,            //show tool tips on cells
      addRowPos:"top",          //when adding a new row, add it to the top of the table
      pagination:"local",       //paginate the data
      //paginationSize:7,         //allow 7 rows per page of data
      paginationCounter:"rows", //display count of paginated rows in footer
      movableColumns:true,      //allow column order to be changed
      resizableRows:true,       //allow row order to be changed
      initialSort:[             //set the initial sort order of the data
          {column:"IFS", dir:"asc"},
      ],
      columns:[                 //define the table columns
        {title:"IFS", field:"IFS", hozAlign:"left", formatter:"plaintext"},
        {title:"type", field:"type", hozAlign:"left", formatter:"plaintext"},
        {title:"dataprovider", field:"dataprovider", hozAlign:"left", formatter:"plaintext"},
        {title:"enabled", field:"enabled",  width:90,  hozAlign:"center", formatter:"tickCross", sorter:"boolean"},
        {title:"online", field:"online",  width:90,  hozAlign:"center", formatter:"tickCross", sorter:"boolean"},
      ],
    });

    table.on("rowDblClick", function(e, row){
      //alert("Cell clicked: " + row.getData() + " "); //test  
      var modalTarget = document.querySelector("#modal-2");
      document.querySelector(".modal-fader").className += " active";
      modalTarget.className += " active";
      
      modalTarget.dataprovider_id = row.getData().id;
      document.querySelectorAll(".modal-delete").forEach(function (deleteBtn) {
        deleteBtn.style.display = "inline-block";
      });
      modalTarget.childNodes[3].value = '{            \n \
  "dataprovider":"' + row.getData().dataprovider + '",\n \
  "enabled": '+ row.getData().enabled +',             \n \
  "IFS": "'+ row.getData().IFS +'",                   \n \
  "type": "'+ row.getData().type +'"                  \n \
}';
    });

    init_add_datapoints();
    refresh_dataproviders_table();
  }
  
  function init_add_datapoints() {
  
    document.querySelectorAll(".open-modal").forEach(function (trigger) {
      trigger.addEventListener("click", function () {
            hideAllModalWindows();
            showModalWindow(this);
        });
    });
  
    document.querySelectorAll(".modal-save").forEach(function (saveBtn) {
      saveBtn.addEventListener("click", function () {
        var modalTarget = document.querySelector("#modal-2");
        let error_msg = document.querySelector('#modal-2_error-message');
        try{
          let dataprovider = modalTarget.childNodes[3].value;
          let temp = JSON.parse(dataprovider);
          socket.emit('edit_dataprovider', dataprovider, 
            function(ret){
              location.reload(); 
              if(ret == true){
                console.log("save ok");
                error_msg.innerHTML = "Saved";
                error_msg.style = "color:green";
              }else{
                alert("could not save dataprovider");
              }
            }
          );
        } catch(err) {
          error_msg.innerHTML = err.message;
          error_msg.style = "color:red";
        }
      });
    });

    document.querySelectorAll(".modal-delete").forEach(function (deleteBtn) {     
      deleteBtn.addEventListener("click", function () {
        var modalTarget = document.querySelector("#modal-2");
        let error_msg = document.querySelector('#modal-2_error-message');
        try{
          if('dataprovider_id' in modalTarget && modalTarget.dataprovider_id[0] === '_'){
            socket.emit('delete_dataprovider', modalTarget.dataprovider_id, 
              function(ret){
                location.reload(); 
                if(ret == true){
                  console.log("save ok");
                  error_msg.innerHTML = "Saved";
                  error_msg.style = "color:green";
                }else{
                  alert("could not delete dataprovider");
                }
              }
            );
          }
          } catch(err) {
            error_msg.innerHTML = err.message;
            error_msg.style = "color:red";
          }
      });
    });
  
    document.querySelectorAll(".modal-hide").forEach(function (closeBtn) {
      closeBtn.addEventListener("click", function () {
            hideAllModalWindows();
        });
    });
  
    document.querySelector(".modal-fader").addEventListener("click", function () {
        hideAllModalWindows();
    });
  
    var btn = document.createElement("button");
    var t = document.createTextNode("add dataprovider");
    btn.setAttribute("class","mapButton");
    btn.appendChild(t);
    document.querySelector("#mmi_svg").parentElement.insertBefore(btn,document.querySelector("#mmi_svg"));//,null);
    btn.addEventListener("click", function () {
        hideAllModalWindows();
        show_add_dataprovider_ModalWindow(this);
      });
  
  }
  
  function show_add_dataprovider_ModalWindow (buttonEl) {
    var modalTarget = document.querySelector("#modal-2");
    document.querySelector(".modal-fader").className += " active";
    modalTarget.className += " active";
  
    document.querySelector('#modal-2_error-message').innerHTML = "";
    document.querySelector('#modal-2_error-message').style = "color:black";

    document.querySelectorAll(".modal-delete").forEach(function (deleteBtn) {
      deleteBtn.style.display = "none";
    });
    modalTarget.childNodes[3].value = '{ \n \
  "dataprovider":"[IP]:[port]",          \n \
  "enabled": [false/true],               \n \
  "IFS": "[IFS name]",                   \n \
  "type": "[Protocol type]"              \n \
}';
  }
  

  