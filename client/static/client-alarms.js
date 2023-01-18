function init_alarm(){
    //define data array
    socket.on('update_alarm_table', function (json) {
        console.log("UPDATE TRIGGER");
        json.forEach((item) => {
          item['b1'] = item['element']['B1'];
          item['b2'] = item['element']['B2'];
          item['b3'] = item['element']['B3'];
          //ret['value']
        });
        table.replaceData(json).then(function(){
          table.getRows().forEach((row_element) => {
            let alarm = row_element.getData().alarm;
            let ack = row_element.getData().acknowledged;
            let open = row_element.getData().open;
            row_element.getElement().style.animation = ""; 
            if(alarm == true && ack == false && open == true){
              row_element.getElement().style.animation = "blinker 1s linear infinite"; 
            } else if(alarm == false && ack == false && open == true){
              row_element.getElement().style.backgroundColor = "orange"; 
              row_element.getElement().style.color = "black"; 
            } else if(alarm == true && ack == true && open == true){
              row_element.getElement().style.backgroundColor = "yellow"; 
              row_element.getElement().style.color = "black"; 
            } else if(alarm == false && ack == true && open == true){
              row_element.getElement().style.backgroundColor = "green"; 
              row_element.getElement().style.color = "black"; 
            }else {
              row_element.getElement().style.backgroundColor = "black"; 
              row_element.getElement().style.color = "white"; 
            }
          });
        }); //load data array
    });
  
  
    var table = new Tabulator("#mmi_svg", {
      //data:tabledata,           //load row data from array
      layout:"fitColumns",      //fit columns to width of table
      responsiveLayout:"hide",  //hide columns that dont fit on the table
      //tooltips:true,            //show tool tips on cells
      addRowPos:"top",          //when adding a new row, add it to the top of the table
      history:true,             //allow undo and redo actions on the table
      pagination:"local",       //paginate the data
      paginationSize:7,         //allow 7 rows per page of data
      paginationCounter:"rows", //display count of paginated rows in footer
      movableColumns:true,      //allow column order to be changed
      resizableRows:true,       //allow row order to be changed
      initialSort:[             //set the initial sort order of the data
          {column:"time", dir:"asc"},
      ],
      columns:[                 //define the table columns
          {title:"Time", field:"time",hozAlign:"center", formatter:"plaintext"},
          {title:"B1", field:"b1", hozAlign:"left", formatter:"plaintext"},
          {title:"B2", field:"b2", hozAlign:"left", formatter:"plaintext"},
          {title:"B3", field:"b3", hozAlign:"left", formatter:"plaintext"},
          {title:"Message", field:"message", hozAlign:"left", formatter:"textarea"},
          {title:"Alarm", field:"alarm", width:90,  hozAlign:"center", formatter:"tickCross", sorter:"boolean", editor:"tickCross" },
          {title:"Ack", field:"acknowledged", width:90,  hozAlign:"center", formatter:"tickCross", sorter:"boolean", editor:"tickCross" },
          {title:"Open", field:"open", width:90,  hozAlign:"center", formatter:"tickCross", sorter:"boolean", editor:"tickCross" },
      ],
    });
  

  
    //only show open alarms
    //table.setFilter("open", "=", "true");
    table.on("cellEdited", function(cell){
      let data = cell.getData();
      //acknowledge alarm/close alarm    
      socket.emit('update_alarm_state', data );
  
      table.refreshFilter();
    });
  
    table.on("cellDblClick", function(e, cell){
      let field = cell.getField();
      if(field === "alarm" || field === "acknowledged" || field === "open"){
        let inv = !cell.getValue();
        cell.setValue(inv);
      }
      else{
        alert("Cell clicked: " + cell.getField() + " "); //test
      }
  
    });
  
    init_editRules();

    refresh_alarm_table();
  }
  
  function refresh_alarm_table(){
    socket.emit('get_alarm_table', {} );
  }
  
  
  function init_editRules() {
  
    document.querySelectorAll(".open-modal").forEach(function (trigger) {
      trigger.addEventListener("click", function () {
            hideAllModalWindows();
            showModalWindow(this);
        });
    });
  
    document.querySelectorAll(".modal-save").forEach(function (saveBtn) {
      saveBtn.addEventListener("click", function () {
        var modalTarget = document.querySelector("#modal-1");
        socket.emit('save_alarm_rules', modalTarget.childNodes[3].value, 
          function(ret){
            console.log("save ok");
          }
        );
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
    var t = document.createTextNode("edit rules");
    btn.setAttribute("class","mapButton");
    btn.appendChild(t);
    document.querySelector("#mmi_svg").parentElement.insertBefore(btn,document.querySelector("#mmi_svg"));//,null);
    btn.addEventListener("click", function () {
        hideAllModalWindows();
        show_edit_alarm_ModalWindow(this);
      });
  
  }
  
  function show_edit_alarm_ModalWindow (buttonEl) {
    var modalTarget = document.querySelector("#modal-1");
    document.querySelector(".modal-fader").className += " active";
    modalTarget.className += " active";
  
    socket.emit('get_alarm_rules', { }, 
      function(ret){
        modalTarget.childNodes[3].value = ret;
      }
    );
  }
  
