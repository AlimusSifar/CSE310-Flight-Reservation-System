// REGISTER - AGREEMENT
document.getElementById("agreement").addEventListener("change", (event) => {
    document.getElementById("register-button").disabled = !event.target.checked;
});

// TABS - FUNCTION
function changeTabStyle(vTabs) {
    vTabs.forEach((tab) => {
        tab.addEventListener("click", () => {
            vTabs.forEach((tb) => {
                if (tab === tb && tab.ariaSelected === "true") tab.classList.add("fw-bold");
                else tb.classList.remove("fw-bold");
            });
        });
    });
}

// TABS
const vTabs = [...document.getElementById("v-tabs-tab").children];
changeTabStyle(vTabs);

// TABS - INNER
const vTabsInner = [...document.getElementById("v-tabs-tab-inner").children];
changeTabStyle(vTabsInner);

// ADMIN DASHBOARD - AIRCRAFT FORM
const inputNumber = document.getElementById("input-aircraft-capacity-number");
const inputRange = document.getElementById("input-aircraft-capacity-range");

inputRange.addEventListener("input", (event) => {
    inputNumber.value = event.target.value;
});

inputNumber.addEventListener("input", (event) => {
    inputRange.value = event.target.value;
});

// REGISTRATION - PASSWORD VALIDATION

// BOOKING CONFIRMATION
function confirm_booking() {
    const cc = document.getElementById("input-booking-creditcard").value;
    if (cc.length !== 16) return true;
    if (!confirm("Do you want to confirm your booking?")) return false;
    alert("Thank you!\nYour booking has been confirmed!");
    return true;
}

// BASE - CLOSE FLASH MESSAGE
function close_flash_message() {
    document.getElementById("flash-message-box").style.display = "none";
}

// // BASE - ALERT AUTO CLOSE
// window.setTimeout(() => {
//     document.getElementById("flash-message-box").style.display = "none";
// }, 5000);
