// $(document).ready(function(){
// 	var form = $('#form_buying_product');

// 	let serviceType = $(this).attr('data-service-type'); //получаем атрибут у кнопки


// 	form.on('submit', function(e){
// 		e.preventDefault();
// 		var submit_btn = $('#submit_btn');
// 		var product_id = submit_btn.data('product_id');
// 		var product_name = submit_btn.data('name');
// 		var product_price = submit_btn.data('price');
// 		console.log(product_id);
// 		console.log(product_name);

// 	})
$(document).ready(function(){
	$('.add-to-cart').on('click', function (e) {
		e.preventDefault();
    	var that = $(this);
    
		var product_id = that.data('product_id');
		var product_name = that.data('name');
		var product_price = that.data('price');
		console.log(product_id);
		console.log(product_name);
});
})