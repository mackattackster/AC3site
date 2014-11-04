$(function() {
    $( "#date1" ).datepicker();
  });
  
 $(function() {
    $( "#date2" ).datepicker();
  });
  
 $( "#sensor" ).selectmenu();
 
 $( "#deactivated" ).selectmenu();
 
 $(document).ready(function(){
var data = JSON.parse(document.getElementById("eventJSON").value);

  var plot1 = jQuery.jqplot ('eventactors', [getUserPercent(data)],
    { 
	  title: 'User Event Occurrence',
      seriesDefaults: {
        // Make this a pie chart.
        renderer: jQuery.jqplot.PieRenderer, 
        rendererOptions: {
          // Put data labels on the pie slices.
          // By default, labels show the percentage of the slice.
          showDataLabels: true
        }
      },
      legend: { show:true, location: 'e' }
    }
  );

  var plot2 = jQuery.jqplot ('sensors', [getSensorPercents(data)],
    { 
	  title: 'Sensor Event Occurrence',
      seriesDefaults: {
        // Make this a pie chart.
        renderer: jQuery.jqplot.PieRenderer, 
        rendererOptions: {
          // Put data labels on the pie slices.
          // By default, labels show the percentage of the slice.
          showDataLabels: true
        }
      },
      legend: { show:true, location: 'e' }
    }
  );
});

function getSensorPercents(event) {
    var i, key;
    var val
    var sensors = {};
    for (i = 0; i < event.length; ++i) {
        key = event[i]['fields']['sensor_triggered'];
        if (event[i]['fields']['sensor_triggered'] && sensors[key] == val) {
            sensors[key] = 1;
        }
        else {
            sensors[key] += 1;
        }
    }
    return getKeys(sensors);
}

function getUserPercent(user) {
    var i, key;
    var val;
    var users = {};
    for (i = 0; i < user.length; ++i) {
        key = user[i]['fields']['user_id'];
        if (user[i]['fields']['user_id'] && users[key] == val) {
            users[key] = 1;
        }
        else {
            users[key] += 1;
        }
    }
    return getKeys(users);
}

function getKeys(o) {
    var i, keys = Object.keys(o);
    var data = [];
    for (i = 0; i < keys.length; i++) {
        data.push([keys[i], o[keys[i]]]);
    }
    return data;
}