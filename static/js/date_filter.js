document.addEventListener("DOMContentLoaded", function () {
  const startInput = document.getElementById("start_date");
  const endInput = document.getElementById("end_date");
  const resetBtn = document.getElementById("resetBtn");
  const filterForm = document.getElementById("filterForm");

  function updateStartAndEndLimits() {
    if (startInput.value) {
      endInput.min = startInput.value;
      if (endInput.value < startInput.value) {
        endInput.value = startInput.value;
      }
    }

    if (endInput.value) {
      startInput.max = endInput.value;
      if (startInput.value > endInput.value) {
        startInput.value = endInput.value;
      }
    }
  }

  if (startInput && endInput) {
    startInput.addEventListener("change", updateStartAndEndLimits);
    endInput.addEventListener("change", updateStartAndEndLimits);

    updateStartAndEndLimits();
  }

  if (resetBtn && filterForm) {
    resetBtn.addEventListener("click", function () {
      startInput.value = "";
      endInput.value = "";
      filterForm.submit();
    });
  }
});
