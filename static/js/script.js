function openClose(element) {
  const icon = element + 'Icon';
  const content = element + 'Content';

  if (document.getElementById(icon).className == 'fa fa-plus-circle fa-2x') {
    document.getElementById(icon).className = 'fa fa-minus-circle fa-2x';
    document.getElementById(content).style.display = 'inline-block';
  } else {
    document.getElementById(icon).className = 'fa fa-plus-circle fa-2x';
    document.getElementById(content).style.display = 'none';
  }
}

function open(element) {
  const icon = element + 'Icon';
  const content = element + 'Content';
  document.getElementById(icon).className = 'fa fa-minus-circle fa-2x';
  document.getElementById(content).style.display = 'inline-block';
}
