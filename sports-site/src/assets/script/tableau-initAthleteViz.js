function initAthleteViz() {
    //grab page element
    var containerDiv = document.getElementsByTagName('app-athletes-page').item(0).getElementsByTagName('div').item(0),
    
    //Tableau public visualization    
    url = "https://public.tableau.com/views/Trackv2/StudentTable?:language=en&:display_count=y&:origin=viz_share_link",
        
    options = {
      height: 800,
      width: 1000,
      hideTabs: true,
  
    //debugging
    onFirstInteractive: function () {
      console.log("Visualization made");
      }
    };
  
    if(viz != null) {
      viz.dispose();
    }
   
    //create a new object, put in container
    var viz = new tableau.Viz(containerDiv, url, options);
  
  }
