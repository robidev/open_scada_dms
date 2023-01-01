function init_events(){

    socket.on('update_event_table', function (json) {
      //write events to table
      table.replaceData(json);
    });
  
    socket.on('add_event_to_table', function (json) {
      //add a event to table
      table.addData(json)
    });
  
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
          {column:"time", dir:"asc"},
      ],
      columns:[                 //define the table columns
          {title:"Time", field:"time",hozAlign:"center", formatter:"plaintext"},
          {title:"Element", field:"element", hozAlign:"left", formatter:"plaintext"},
          {title:"Message", field:"msg", hozAlign:"left", formatter:"textarea"},
          {title:"Value", field:"value", hozAlign:"left", formatter:"plaintext"},
      ],
    });
  
    refresh_event_table();
  }
  
  function refresh_event_table(){
    socket.emit('get_event_table', {} );
  }
  