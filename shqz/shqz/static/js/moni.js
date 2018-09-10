//var str2 = "js实现用{1}自符串替换占位符{1} {2}  {0} ".format("I","LOVE","YOU");
String.prototype.format = function() {
    if(arguments.length == 0) return this;
    var param = arguments[0];
    var s = this;
    if(typeof(param) == 'object') {
     for(var key in param)
      s = s.replace(new RegExp("\\{" + key + "\\}", "g"), param[key]);
     return s;
    } else {
     for(var i = 0; i < arguments.length; i++)
      s = s.replace(new RegExp("\\{" + i + "\\}", "g"), arguments[i]);
     return s;
    }
}
function qn(){
    $zyzs = $('#zyzs').val();
    $zydj = $('#zydj').val();
    $zyhqn = $('#zyhqn').val();
    $sxll = $('#sxll').val(Number($zydj)+10);
    $sxtz = $('#sxtz').val(Number($zydj)+10);
    $sxxl = $('#sxxl').val(Number($zydj)+10);
    $sxmj = $('#sxmj').val(Number($zydj)+10);
    $sxnl = $('#sxnl').val(Number($zydj)+10);
    if($zyzs==0){
        var sxzqn = $zydj*5
    }else if($zyzs==1){
        var sxzqn = 125*5 + ($zydj-125)*6
    }else if($zyzs==2){
        var sxzqn = 125*5 + ($zydj-125)*7
    }else if($zyzs==3){
        var sxzqn = 125*5 + ($zydj-125)*8
    }else if($zyzs==4){
        var sxzqn = 125*5 + ($zydj-125)*9
    }else if($zyzs==5){
        var sxzqn = 125*5 + ($zydj-125)*10
    }
    sxzqn += Number($zyhqn)
    $('#sxzqn').val(sxzqn);
}
function fpsx(){
    $zqn = $('#sxzqn').val();
    $fpll = $('#fpll').val();
    $fptz = $('#fptz').val();
    $fpxl = $('#fpxl').val();
    $fpmj = $('#fpmj').val();
    $fpnl = $('#fpnl').val();
    $sxll = $('#sxll').val();
    $sxtz = $('#sxtz').val();
    $sxxl = $('#sxxl').val();
    $sxmj = $('#sxmj').val();
    $sxnl = $('#sxnl').val();
    if(Number($fpll)+Number($fpmj)+Number($fpnl)+Number($fptz)+Number($fpxl)==$zqn){
        $('#sxzqn').val(0);
        $('#sxll').val(Number($fpll)+Number($sxll));
        $('#sxxl').val(Number($sxxl)+Number($fpxl));
        $('#sxnl').val(Number($sxnl)+Number($fpnl));
        $('#sxtz').val(Number($sxtz)+Number($fptz));
        $('#sxmj').val(Number($sxmj)+Number($fpmj));
    }else{
        alert('潜能未正确分配')
    }
}
function zyxz(){
    //return [hp, sp, 攻击,命中,灵巧, 闪避,防御,L精神,T精神,N精神,X精神]
    //        0   1    2   3   4    5   6    7    8     9    10
    //        T   X    L   L   M    M   N   L     T    N     X
    $zyzy = $('#zyzy').val()
    // 1剑客 2术士 3武师 4道士 5浪子 6医师
    if($zyzy==1){
        return [6.9,2.4,1.05,1.26,0.64,1.22,0.8,0.15,0.15,0.15,0.7]
    }else if($zyzy==2){
        return [4.5,4.5,0.7,0.8,0.7,1.2,0.8,0.26,0.26,0.26,1.3]
    }else if($zyzy==3){
        return [6.0,2.4,1.1,1.1,0.75,1.2,0.8,0.2,0.2,0.2,1.0]
    }else if($zyzy==4){
        return [6.0,3.6,0.9,0.9,0.7,1.0,0.85,0.22,0.22,0.22,1.15]
    }else if($zyzy==5){
        return [5.7,3.3,0.97,1.0,0.75,1.0,0.95,0.2,0.2,0.2,1.0]
    }else if($zyzy==6){
        return [7.2,3.6,1.075,0.9,0.64,1.1,0.8,0.22,0.22,0.22,1.1]
    // 11剑圣 21法王 31武神 41道祖 51游仙 61神医
    }else if($zyzy==11 || $zyzy==111 || $zyzy==112){
        return [7.59,2.64,1.155,1.386,0.704,0.99,1.342,0.15,0.165,0.165,0.77]
    }else if($zyzy==21 || $zyzy==211 || $zyzy==212){
        return [4.95,4.95,0.77,0.88,0.77,1.32,0.88,0.286,0.286,0.286,1.43]
    }else if($zyzy==31 || $zyzy==311 || $zyzy==312){
        return [6.6,2.64,1.21,1.21,0.825,1.22,0.88,0.22,0.22,0.22,1.1]
    }else if($zyzy==41 || $zyzy==411 || $zyzy==412){
        return [6.6,3.96,0.99,0.99,0.77,1.1,0.935,0.242,0.242,0.242,1.126]
    }else if($zyzy==51 || $zyzy==511 || $zyzy==512){
        return [6.27,3.63,1.067,1.1,0.825,1.1,1.045,0.22,0.22,0.2,1.1]
    }else if($zyzy==61 || $zyzy==611 || $zyzy==612){
        return [7.92,3.96,1.182,0.99,0.704,1.21,0.88,0.242,0.242,0.242,1.21]
    }
}
function main(){
    $sxll = $('#sxll').val();
    $sxtz = $('#sxtz').val();
    $sxxl = $('#sxxl').val();
    $sxmj = $('#sxmj').val();
    $sxnl = $('#sxnl').val();
    var sxsz = zyxz()
    $hp = $('#hp').val();
    $sp = $('#sp').val();
    $gj = $('#gj').val();
    $mz = $('#mz').val();
    $lq = $('#lq').val();
    $sb = $('#sb').val();
    $fy = $('#fy').val();
    $js = $('#js').val();
    $('#hp').val(Number($hp)+sxsz[0]*$sxtz);
    $('#sp').val(Number($sp)+sxsz[1]*$sxxl);
    $('#gj').val(Number($gj)+sxsz[2]*$sxll);
    $('#mz').val(Number($mz)+sxsz[3]*$sxll);
    $('#lq').val(Number($lq)+sxsz[4]*$sxmj);
    $('#sb').val(Number($sb)+sxsz[5]*$sxmj);
    $('#fy').val(Number($fy)+sxsz[6]*$sxnl);
    $('#js').val(Number($js)+Number(sxsz[7]*$sxll)+Number(sxsz[8]*$sxtz)+
                 Number(sxsz[9]*$sxnl)+Number(sxsz[10]*$sxxl));
}
function mainxs(){
    $zyzy = $('#zyzy').val()
    // 111剑仙 112剑魔 211法神 212魔王 311武魂 312武痴 411天师 412道圣
    if($zyzy==111){
        $('#sxll').val($('#sxll').val()*1.05);
        $('#sxtz').val($('#sxtz').val()*0.95);
        main()
    }else if($zyzy==112){
        $('#sxll').val($('#sxll').val()*0.95);
        $('#sxtz').val($('#sxtz').val()*1.05);
        main()       
    }else if($zyzy==211){
        $('#sxmj').val($('#sxmj').val()*1.05);
        $('#sxnl').val($('#sxnl').val()*0.95);
        main()
    }else if($zyzy==212){
        $('#sxtz').val($('#sxtz').val()*0.95);
        $('#sxxl').val($('#sxxl').val()*1.05);
        main()       
    }else if($zyzy==311){
        $('#sxmj').val($('#sxmj').val()*1.05);
        $('#sxll').val($('#sxll').val()*0.95);
        main()
    }else if($zyzy==312){
        $('#sxmj').val($('#sxmj').val()*0.95);
        $('#sxll').val($('#sxll').val()*1.05);
        main()       
    // 411天师 412道圣 511潜影 512邪影 611仁心 612巫医
    }else if($zyzy==411){
        $('#sxll').val($('#sxll').val()*1.05);
        $('#sxmj').val($('#sxmj').val()*0.95);
        main()
    }else if($zyzy==412){
        $('#sxxl').val($('#sxxl').val()*0.95);
        $('#sxmj').val($('#sxmj').val()*1.05);
        main()
    }else if($zyzy==511){
        $('#sxll').val($('#sxll').val()*1.05);
        $('#sxxl').val($('#sxxl').val()*0.95);
        main()
    }else if($zyzy==512){
        $('#sxll').val($('#sxll').val()*0.95);
        $('#sxxl').val($('#sxxl').val()*1.05);
        main()
    }else if($zyzy==611){
        $('#sxtz').val($('#sxtz').val()*1.05);
        $('#sxxl').val($('#sxxl').val()*0.95);
        main()
    }else if($zyzy==612){
        $('#sxtz').val($('#sxtz').val()*0.95);
        $('#sxxl').val($('#sxxl').val()*1.05);
        main()
    }
}

function ces(){
    var arr = ['tk','yd','yf','hw','xz','wq','xl','jz','mj','pf',
               'wz','zq','fy','hy','xs','hjj','xs'];
    var dj = Number($('#zydj').val())+10;
    var ll1 = 0;
    var tz1 = 0;
    var xl1 = 0;
    var mj1 = 0;
    var nl1 = 0;
    for(i=0;i<arr.length;i++){
        var ll = eval("$('#{0}ll').val();".format(arr[i]));
        ll1 += Number(ll);
        var tz = eval("$('#{0}tz').val();".format(arr[i]));
        tz1 += Number(tz);
        var xl = eval("$('#{0}xl').val();".format(arr[i]));
        xl1 += Number(xl);
        var mj = eval("$('#{0}mj').val();".format(arr[i]));
        mj1 += Number(mj);
        var nl = eval("$('#{0}nl').val();".format(arr[i]));
        nl1 += Number(nl);
    };
    $('#sxll').val(ll1+dj);
    $('#sxtz').val(tz1+dj);
    $('#sxxl').val(xl1+dj);
    $('#sxmj').val(mj1+dj);
    $('#sxnl').val(nl1+dj);
}