gsap.from("#sec_2 h1",{
    opacity:0,
    duration:1,
    scrollTrigger:{
        trigger:"#sec_2 h1",
        scroller:"body",
        start:"top 60%",
        end:"bottom top",
        markers:true,
    }
});