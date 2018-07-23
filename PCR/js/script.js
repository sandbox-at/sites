
// Immediately Invoking Function Expression - IIFE
(function(){
	
	// Storing the reference of mobile drawer in a variable
	var mobileMenuDrawer = document.querySelector(".mobile-menu");
	
	// Attaching a click event to mobile Drawer
	mobileMenuDrawer.addEventListener("click", function(){
		var mobileMenuItem = document.querySelector(".menu-list-item");

		if(mobileMenuItem.style.display == "none"){
			mobileMenuItem.style.display = "block";
		} else{
			mobileMenuItem.style.display = "none";
		}
	});


})();
