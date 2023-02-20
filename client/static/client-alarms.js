function init_alarm(){
    //define data array
    socket.on('update_alarm_table', function (json) {
        console.log("UPDATE TRIGGER");
        table.replaceData(json).then(function(){
          table.getRows().forEach((row_element) => {
            let alarm = row_element.getData().alarm;
            let ack = row_element.getData().acknowledged;
            let open = row_element.getData().open;

            let severity = row_element.getData().severity;
            row_element.getElement().style.animation = ""; 
            if(alarm == true && ack == false && open == true){
              if(severity == 0) {      row_element.getElement().style.animation = "blinker_info 1s linear infinite"; }
              else if (severity == 1) {row_element.getElement().style.animation = "blinker_low 1s linear infinite"; }
              else if (severity == 2) {row_element.getElement().style.animation = "blinker_medium 1s linear infinite"; }
              else if (severity == 3) {row_element.getElement().style.animation = "blinker_high 1s linear infinite"; }
              else if (severity == 4) {row_element.getElement().style.animation = "blinker_critical 1s linear infinite"; }
              else{                    row_element.getElement().style.animation = "blinker_high 1s linear infinite"; }
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
          {title:"Element", field:"element", hozAlign:"left", formatter:"plaintext"},
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
      document.querySelector("#alarm_comment").value = "";
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
        hideAllModalWindows();
        let row = cell.getRow();
        //alert("Cell clicked: " + cell.getField() + " : " + row.getData().details); //test, should become modal html dialog
        let modalAlarmTarget = document.querySelector("#modal-alarm");
        document.querySelector(".modal-fader").className += " active";
        modalAlarmTarget.className += " active";
        document.querySelector("#modal-alarm-time").innerHTML = "<b>Time:</b>" + row.getData().time;
        document.querySelector("#modal-alarm-severity").innerHTML = "<b>Severity:</b>" + row.getData().severity;
        document.querySelector("#modal-alarm-element").innerHTML = "<b>Element:</b>" + row.getData().element;
        document.querySelector("#modal-alarm-datapoint").innerHTML = "<b>Datapoint:</b>" + row.getData().datapoint;
        document.querySelector("#modal-alarm-value").innerHTML = "<b>Value:</b>" + row.getData().value;
        document.querySelector("#modal-alarm-message").innerHTML = "<b>Message:</b>" + row.getData().message;
        document.querySelector("#modal-alarm-details").innerHTML = row.getData().details;
        document.querySelector("#alarm_comment").value = "";
        var currentRow = row.getData()
        document.querySelector("#modal-silence-alarm").onclick = function () {
          currentRow.alarm = false;
          currentRow.comment = document.querySelector("#alarm_comment").value;
          socket.emit('update_alarm_state', currentRow );
          table.refreshFilter();
          hideAllModalWindows();
        };
        document.querySelector("#modal-ack-alarm").onclick = function () {
          currentRow.acknowledged = true;
          currentRow.comment = document.querySelector("#alarm_comment").value;
          socket.emit('update_alarm_state', currentRow );
          table.refreshFilter();
          hideAllModalWindows();
        };
    
        document.querySelector("#modal-close-alarm").onclick = function () {
          currentRow.open = false;
          currentRow.comment = document.querySelector("#alarm_comment").value;
          socket.emit('update_alarm_state', currentRow );
          table.refreshFilter();
          hideAllModalWindows();
        };
      }
  
    });
  
    document.querySelector(".modal-fader").addEventListener("click", function () {
        hideAllModalWindows();
    });

    init_alarm_dialog();
    init_editRules();

    refresh_alarm_table();
  }
  
  function refresh_alarm_table(){
    socket.emit('get_alarm_table', {} );
  }

  function init_alarm_dialog() {
    document.querySelectorAll(".aPop-close").forEach(function (closeBtn) {
      closeBtn.addEventListener("click", function () {
          document.querySelector("#alarm_comment").value = "";
          hideAllModalWindows();
        });
    });
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
        let error_msg = document.querySelector('#modal-1_error-message');
        try{
          let rules = modalTarget.childNodes[3].value;
          let temp = JSON.parse(rules);
          socket.emit('save_alarm_rules', rules, 
            function(ret){ 
              if(ret == true){
                console.log("save ok");
                error_msg.innerHTML = "Saved";
                error_msg.style = "color:green";
              }else{
                alert("could not save alarm rules");
              }
            }
          );
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

    document.querySelector('#modal-1_error-message').innerHTML = "";
    document.querySelector('#modal-1_error-message').style = "color:black";
  
    socket.emit('get_alarm_rules', { }, 
      function(ret){
        modalTarget.childNodes[3].value = ret;
      }
    );
  }
  
