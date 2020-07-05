function AddPlantHumidity(){

    const newPlantHumidity = {
        name : $('#plantName').val(),
        opt_Humidity: parseFloat($('#plantHumidity').val())
    };
    console.log(JSON.stringify(newPlantHumidity))

    $.ajax(
        {
            url: 'http://localhost:5000/add/plant/',
            method: 'POST',
            data: JSON.stringify(newPlantHumidity),
            dataType: 'json',
            contentType: "application/json",
            success: function (data) {
                $('#plantName').val('');
                $('#plantHumidity').val('');
                var tablePlantHumidity = $('#dataTable2').DataTable();
                
                var row = tablePlantHumidity.row.add([
                        newPlantHumidity.name,
                        newPlantHumidity.opt_Humidity
                    ]).draw();

                $('#exampleModalCenter').modal("hide");
                swal('Added',"","success");
            },
            error:function(err){
                swal('Error happened!',"","error");
            }
        })
    };



function LoadPlantHumidityData(){
   
    $.ajax(
        {
            url: 'http://localhost:5000/plant/',
            method: 'GET',
            contentType: "application/json",
            success: function (data) {
                var tablePlantHumidity = $('#dataTable2').DataTable();
                tablePlantHumidity.rows().remove().draw();
                data = JSON.parse(data)
                    $.each(data, function (i,item) {
                        tablePlantHumidity.row.add([
                            item.name,
                            item.opt_humidity
                        ]).draw();
                    });
            },
            error:function(err){
                swal('Error happened!',"","error");
            }
        });
}