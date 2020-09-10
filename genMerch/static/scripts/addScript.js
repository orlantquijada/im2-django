$(document).ready(function(){
   
    appendElem();
});


function appendElem(){
    alert("OKAY");
    var elem1 =  '<div class="form-row"> \
                      <div class="col-2"> \
                        &nbsp;&nbsp; <label>School</label></div>  \
                        <div class="col-10 mx-0"> \
                          <input type="text" class="form-control" id="elemSchool"/> \
                          </div> </div> \
                          <div class="form-row">\
                    <div class="col-2">&nbsp; &nbsp;<label>Grade</label></div>\
                    <div class="col-10 mx-0">\
                      <input\
                        type="number"\
                        class="form-control"\
                        id="elemGrade"\
                      />\
                    </div>\
                  </div>\
                  <div class="form-row">\
                    <div class="col-2">\
                      &nbsp; &nbsp;<label>Year Completed</label>\
                    </div>\
                    <div class="col-10 mx-0">\
                      <input\
                        type="number"\
                        class="form-control"\
                        id="elemGraduated"\
                      />\
                    </div>\
                  </div>\
                  <div class="form-row">\
                    <div class="col-2">\
                      &nbsp; &nbsp;<label>Awards</label>\
                    </div>\
                    <div class="col-10 mx-0">\
                      <textarea\
                        class="form-control"\
                        id="elemSchool"\
                        rows="3"\
                      ></textarea>\
                    </div>\
                  </div>'
        
    $("#elem").append(elem1);

}