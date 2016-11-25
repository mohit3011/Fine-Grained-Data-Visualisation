function mufunc() {
		var fileInput = document.getElementById('fileInput');

		fileInput.addEventListener('change', function(e) {
			var file = fileInput.files[0];
			var textType = /text.*/;

			if (file.type.match(textType)) {
				var reader = new FileReader();
				reader.onload = function(e) {
					//alert(reader.result);
					//fileDisplayArea.innerText = reader.result;
					var a=reader.result;
					b=a.split('\n');
					var c=[];
					for(var i=0;i<b.length;i++)
					{
						c.push(b[i].split(' '));
					}
					alert(c);
				}

				reader.readAsText(file);
			} else {

			}
		});
}
