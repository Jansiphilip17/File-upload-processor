<template>
  <div>
    <h2>Upload PDF or CSV</h2>

    <input type="file" @change="uploadFile" />
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "FileUpload",

  methods: {
  uploadFile(event) {
  const formData = new FormData();
  formData.append("file", event.target.files[0]);

  axios.post("http://localhost:8000/upload/pdf/", formData, {
    headers: { "Content-Type": "multipart/form-data" }
  })
  .then(res => console.log("Uploaded", res))
  .catch(err => console.log("Upload Error:", err));
}
  },
};
</script>
