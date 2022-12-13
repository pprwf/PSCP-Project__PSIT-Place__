function showImgPreview(url_link) {
    $(".preview-container").show();
    $("#prev-img").attr("src", url_link)}

function hidePreview() {$(".preview-container").hide();}

function showAlert(mess) {
    Swal.fire({position: "center", icon: "success", title: "", text: mess, showConfirmButton: false, timer: 5000})}

function delay (URL, ms) {
    setTimeout( function() { window.location = URL }, ms);}
