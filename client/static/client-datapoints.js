function init_dataproviders(){

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
  
    refresh_dataproviders_table();
  }
  

  