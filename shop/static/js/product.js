function showImgPreview() {
    $(".preview-container").show();
    $("#prev-img").attr("src", "https://www.jib.co.th/img_master/product/original/20220316131926_52116_66_1.jpg")}

function hidePreview() {$(".preview-container").hide();}

function showAlert(mess) {
    Swal.fire({position: "center", icon: "success", title: "", text: mess, showConfirmButton: false, timer: 5000})}

function delay (URL, ms) {
    setTimeout( function() { window.location = URL }, ms);}
