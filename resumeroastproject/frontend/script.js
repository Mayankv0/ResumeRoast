const dropArea = document.querySelector(".drag-area"),
  dragText = dropArea.querySelector("header"),
  button = dropArea.querySelector("#actionButton"),
  input = dropArea.querySelector("input"),
  uploadInfo = dropArea.querySelector(".upload-info"),
  orText = dropArea.querySelector("span"),
  loading = document.getElementById("loading"),
  outputBox = document.getElementById("outputBox");
let file;

outputBox.style.display = 'block';
outputBox.textContent = "Upload a resume to get roasted, only if you can handle it";

button.onclick = () => {
  input.click();
};

input.addEventListener("change", function() {
  if (this.files.length > 1) {
    alert("You can only upload one file.");
    return;
  }
  file = this.files[0];
  if (file.size > 2 * 1024 * 1024) {
    alert("File size exceeds 2MB limit.");
    return;
  }
  if (!file.type.includes("pdf")) {
    alert("This is not a PDF File!");
    return;
  }
  dropArea.classList.add("active");
  showFile();
});

dropArea.addEventListener("dragover", (event) => {
  event.preventDefault();
  dropArea.classList.add("active");
  dragText.textContent = "Release to Upload PDF";
});

dropArea.addEventListener("dragleave", () => {
  dropArea.classList.remove("active");
  dragText.textContent = "Drag & Drop your Resume";
});

dropArea.addEventListener("drop", (event) => {
  event.preventDefault();
  if (event.dataTransfer.files.length > 1) {
    alert("You can only upload one file.");
    return;
  }
  file = event.dataTransfer.files[0];
  if (file.size > 2 * 1024 * 1024) {
    alert("File size exceeds 2MB limit.");
    return;
  }
  if (!file.type.includes("pdf")) {
    alert("This is not a PDF File!");
    return;
  }
  showFile();
});

function showFile() {
  let fileType = file.type;
  let validExtensions = ["application/pdf"];
  if (validExtensions.includes(fileType)) {
    let fileReader = new FileReader();
    fileReader.onload = () => {
      let fileURL = fileReader.result;
      let embedTag = `<iframe src="${fileURL}" type="application/pdf"></iframe>`;
      uploadInfo.innerHTML = embedTag;
      dragText.textContent = "Resume Uploaded Successfully";
      orText.style.display = 'none';
      loading.style.display = 'block';
      outputBox.style.display = 'block';
      outputBox.textContent = "Wait while we are preparing for the roast";

      uploadFile(); // Call to start uploading the file
    };
    fileReader.readAsDataURL(file);
  } else {
    alert("This is not a PDF File!");
    dropArea.classList.remove("active");
    dragText.textContent = "Drag & Drop your Resume";
  }
}

async function uploadFile() {
  const fileInput = document.querySelector('input[type="file"]');
  const file = fileInput.files[0];
  const loading = document.getElementById('loading');
  const outputBox = document.getElementById('outputBox');

  if (!file) {
    console.error('No file selected.');
    outputBox.textContent = "No file selected. Please upload a PDF.";
    return;
  }

  const formData = new FormData();
  formData.append("file", file, file.name);

  loading.style.display = 'block';
  outputBox.textContent = "Wait while we are preparing for the roast";

  try {
    const response = await fetch('http://127.0.0.1:5000/upload', {
      method: 'POST',
      body: formData
    });

    if (response.ok) {
      const data = await response.json();
      console.log('Upload successful:', data);

      if (data.roast) {
        outputBox.textContent = data.roast; // Correctly reference the roast result
      } else {
        console.error('No roast data in response:', data);
        outputBox.textContent = "Failed to get roast. Please try again.";
      }
    } else {
      console.error('Upload failed:', response.statusText);
      outputBox.textContent = "Failed to get roast. Please try again.";
    }
  } catch (error) {
    console.error('Error uploading file:', error);
    outputBox.textContent = "Error occurred while uploading. Please try again.";
  } finally {
    loading.style.display = 'none';
  }
}

function showRoastResult(roast) {
  document.getElementById('outputBox')
  console.log('Roast Result:', roast); // Log the result to the console
  outputBox.textContent = roast; // Display the roast result
}
