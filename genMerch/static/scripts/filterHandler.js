class FilterHandler {
  constructor() {
    this.isShowing = null;
    this.popOvers = null;
    this.filterButtons = document.querySelectorAll(".filter-option");
  }

  addEventListeners() {
    this.filterButtons.forEach((btn) => {
      btn.addEventListener("click", (event) => {
        event.stopPropagation();
        this.removeShowingPopovers();
        btn.nextElementSibling.classList.add("filter-search--hide");
        btn.nextElementSibling.classList.add("filter-search--show");
      });
    });

    window.addEventListener("click", this.removeShowingPopovers);

    const showingPopovers = document.querySelectorAll(".filter-search");

    if (showingPopovers !== null) {
      showingPopovers.forEach((popOver) => {
        popOver.addEventListener("click", (event) => {
          event.stopPropagation();
        });
      });
    }
  }

  removeShowingPopovers() {
    const showingPopovers = document.querySelectorAll(".filter-search--show");

    if (showingPopovers !== null) {
      showingPopovers.forEach((popOver) => {
        popOver.classList.remove("filter-search--show");
        popOver.classList.add("filter-search--hide");
      });
    }
  }

  load() {
    this.addEventListeners();
  }
}

const filterHandler = new FilterHandler();
filterHandler.load();
