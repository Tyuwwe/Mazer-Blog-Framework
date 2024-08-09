<script setup>
import CopyRight from '../components/CopyRight.vue'
import VueMarkdownEditor from '@kangc/v-md-editor';
import createKatexPlugin from '@kangc/v-md-editor/lib/plugins/katex/npm';
import enUS from '@kangc/v-md-editor/lib/lang/en-US';

VueMarkdownEditor.use(createKatexPlugin());
VueMarkdownEditor.lang.use('en-US', enUS);
</script>
<template>
  <div class="editor-container">
    <v-md-editor v-model="text" height="600px"
      left-toolbar="undo redo clear | h bold italic strikethrough quote | ul ol table hr | link image code | save"
      right-toolbar="preview toc sync-scroll"
      default-fullscreen=true
      default-show-toc=true
      :disabled-menus="[]" 
      @upload-image="handleUploadImage" />
  </div>
  <CopyRight />
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      text: '',
    };
  },
  methods: {
    async uploadImageReq(file) {
      const formData = new FormData();
      formData.append('file', file[0]);
      let res = axios.post(this.$server + "/api/uploadImage", formData, {
        headers: {
          'Authorization': 'Bearer ' + localStorage.getItem('jwt')
        }
      })
      return res;
    },
    async handleUploadImage(event, insertImage, file) {
      console.log(file)
      let res_img = await this.uploadImageReq(file);
      console.log(res_img)

      insertImage({
        url: this.$server + res_img.data.url,
        desc: file[0].name
      });
    },
  },
};
</script>

<style>
.editor-container {
  width: 100%;
  margin-top: 100px;
  margin-bottom: 100px;
  position: absolute;
  z-index: 100;
  display: flex;
  justify-content: center;
  align-items: center;
}

.editor-container .v-md-editor {
  max-width: 1200px;
  min-width: 400px;
  width: 100%;
}

/* V-Markdown-Editor Theme Override */
.v-md-editor,
.v-md-textarea-editor {
  background-color: var(--bs-body-bg) !important;
  color: var(--bs-primary-text) !important;
}

.vuepress-markdown-body,
.v-md-editor__toolbar-item {
  background-color: var(--bs-body-bg) !important;
  color: var(--bs-primary-text) !important;
}

.v-md-textarea-editor textarea {
  background-color: var(--bs-body-bg) !important;
  color: var(--bs-primary-text) !important;
}

.v-md-editor__toolbar-item:hover {
  background-color: var(--bs-secondary-bg) !important;
}

.v-md-editor__toolbar-item--active,
.v-md-editor__toolbar-item--active:hover {
  background-color: var(--bs-secondary-bg) !important;
}

.v-md-editor__left-area-title,
.v-md-editor__toc-nav-item {
  color: var(--bs-primary-text) !important;
}

.v-md-editor--fullscreen {
  top: 80px !important;
  max-width: 100vw !important;
}
</style>