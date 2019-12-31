document.addEventListener('DOMContentLoaded', function () {
  if (!document.querySelector) { return }
  if (!document.querySelectorAll) { return }

  var display;

  document.querySelector('#appearances .more').style.display = 'block';
  document.querySelectorAll('#appearances .archived').forEach(function (element) {
    display = element.style.display;
    element.style.display = 'none';
  });

  document.querySelector('#appearances .more a').addEventListener('click', function (event) {
    event.preventDefault();
    document.querySelector('#appearances .more').style.display = 'none';
    document.querySelectorAll('#appearances .archived').forEach(function (element) {
      element.style.display = display;
    });
  });
});
