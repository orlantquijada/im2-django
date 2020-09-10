const mainContent = document.querySelector(".main-content .container");
const formContainers = document.querySelector(".bg-color--gray .container");

const gsapFadeUpAnimation = {
  y: 50,
  opacity: 0,
  ease: "power2",
  duration: 1,
  delay: 0.1,
};

if (formContainers !== null) {
  gsap.from(formContainers, gsapFadeUpAnimation);
}

if (mainContent !== null) {
  gsap.from(mainContent, gsapFadeUpAnimation);
}
