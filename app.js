
var cursor = document.querySelector("#cursor");
var main = document.querySelector("body");
const logo = document.querySelector(".btn");
const dropdown = document.querySelector("#ic-log");


gsap.from("nav",{
    opacity:0,
    duration:2
});


main.addEventListener("mousemove",function(dets){
    gsap.to(cursor,{
        x:dets.x,
        y:dets.y,
        ease:"back.out",
        duration:1
    })
})

gsap.to("#logoname h1",{
    transform:"translateX(-55%)",
    scrollTrigger:{
        trigger:"#logoname",
        scroller:"body",
        start:"top 5%",
        end:"top -100%",
        scrub:2,
        pin:true,
    }
})

gsap.from(".circle",{
    opacity:0,
    y:20
})

gsap.from(".signin",{
    opacity:0,
    y:20
})

logo.addEventListener("onclick",()=>{
    gsap.to(dropdown,{
        opacity:"100"
    })
})

function show(){
    dropdown.style.overflow = "visible";
};