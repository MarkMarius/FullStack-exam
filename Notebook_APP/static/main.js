const showMenu = (oMenuToggleID, navLinksID) => {
	const oMenuToggle = document.getElementById(oMenuToggleID),
			navLinks  = document.getElementById(navLinksID);
	if(oMenuToggle && navLinks) {
		oMenuToggle.addEventListener('click', () => {
			navLinks.classList.toggle('show');
		})
	}
}

showMenu("open-menu-toggle", "nav-links");


const removeMenu = (cMenuToggleID, cnavLinksID) => {
	const cMenuToggle = document.getElementById(cMenuToggleID),
			cnavLinks  = document.getElementById(cnavLinksID);
	if(cMenuToggle && cnavLinks) {
		cMenuToggle.addEventListener('click', () => {
			cnavLinks.classList.remove('show');
		})
	}
}

showMenu("close-menu-toggle", "nav-links");


const showCategoryModal = (showSubModalToggleID, subModalID) => {
	const showSubModalToggle = document.getElementById(showSubModalToggleID),
			subModal = document.getElementById(subModalID);

	if(showSubModalToggle && subModal) {
		showSubModalToggle.addEventListener('click', () => {
			subModal.classList.toggle('show_main_category_adder_container')
		})
	}
}

showCategoryModal("bx-plus-circle", "main-category-adder-container")


const closeCategoryModal = (closeSubModalToggleID, subModalID) => {
	const closeSubModalToggle = document.getElementById(closeSubModalToggleID),
			subModal = document.getElementById(subModalID);

	if(closeSubModalToggle && subModal) {
		closeSubModalToggle.addEventListener('click', () => {
			subModal.classList.remove('show_main_category_adder_container')
		})
	}
}

closeCategoryModal("bx-message-square-x", "main-category-adder-container")


