var swi = document.getElementById("swi");
var but = document.getElementById("but");
handle();
swi.onclick=function(){
  if(swi.innerText=="切换为科学型"){
    swi.innerText="切换为标准型";
    but.style.display="none";
  }else{
    swi.innerText="切换为科学型";
    but.style.display="block";
  }
}
function handle(){
  var arr = but.children;
  for(var i=0;i<arr.length;i++){
    arr[i].onclick=function(){
      console.log(this.innerText);
    }
  }
}