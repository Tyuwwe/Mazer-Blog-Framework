<script setup>
import CopyRight from '../components/CopyRight.vue'
import VueMarkdownEditor, { values } from '@kangc/v-md-editor';
import createKatexPlugin from '@kangc/v-md-editor/lib/plugins/katex/npm';
import enUS from '@kangc/v-md-editor/lib/lang/en-US';

VueMarkdownEditor.use(createKatexPlugin());
if (localStorage.getItem('lang') == 'en') {
  VueMarkdownEditor.lang.use('en-US', enUS);
}
</script>
<template>
  <div class="editor-container">
    <v-md-editor v-model="text" height="600px"
      left-toolbar="undo redo clear | h bold italic strikethrough quote | ul ol table hr | link image code | openFileToolbar save commitToolbar settingToolbar"
      right-toolbar="preview toc sync-scroll"
      :default-fullscreen=true
      :default-show-toc=true
      :disabled-menus="[]" 
      :toolbar="toolbar"
      @upload-image="handleUploadImage"
      @save="saveArticle" />
  </div>

  <div class="modal fade" id="createModel" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5 text-reset">{{ $t('editor.modal_title') }}</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div class="form-floating mb-3">
            <input v-model="submitForm.title" type="text" class="form-control" id="floatingTitle" placeholder="Title">
            <label for="floatingTitle">{{ $t('editor.modal_form_title') }}</label>
          </div>
          <div class="form-floating mb-3">
            <input v-model="submitForm.tags" type="text" class="form-control" id="floatingTags" placeholder="Article Tags">
            <label for="floatingTags">{{ $t('editor.modal_form_tags') }}</label>
          </div>
          <div class="form-floating mb-3">
            <select class="form-select" aria-label="selectLang" v-model="submitForm.lang" id="selectLangOptions">
              <option value="zh">中文 (简体)</option>
              <option value="en">English (US)</option>
            </select>
            <label for="selectLangOptions">{{ $t('editor.modal_form_selectlang') }}</label>
          </div>
          <div class="input-group mb-3">
            <button @click="uploadCover()" class="btn btn-outline-secondary" type="button" id="button-addon1">{{ $t('editor.modal_form_upload') }}</button>
            <input id="coverIptVis" type="text" class="form-control" :placeholder="submitForm.cover_url" aria-label="Article Cover" aria-describedby="button-addon1" disabled>
          </div>
          <div class="form-floating">
            <input type="text" readonly class="form-control-plaintext" id="floatingPlaintextInput" :placeholder="submitForm.auid" :value="submitForm.auid">
            <label for="floatingPlaintextInput">{{ $t('editor.modal_form_auid') }}</label>
          </div>
        </div>
        <div class="modal-footer">
          <button type="submit" class="btn btn-primary" @click="submitMeta()">{{ $t('editor.modal_form_submit') }}</button>
        </div>
      </div>
    </div>
  </div>

  <button id="modalHideBtn" style="display: none;" type="button" data-bs-toggle="modal" data-bs-target="#createModel"></button>
  <input ref="file" id="coverIptHid" style="display: none;" type="file" @change="getFileData">
  <input accept=".md" ref="mdFile" id="mdFileIptHid" style="display: none;" type="file" @change="getMarkdownLocal">

  <CopyRight />
</template>

<script>
import axios from 'axios';
import { toRaw } from '@vue/reactivity'

let auid = ''
let server = ''
let newEmptyFile =  new File([""], "")

export default {
  data() {
    return {
      text: '',
      submitForm: {
        title: '',
        auid: '',
        lang: '',
        tags: '',
        cover_url: this.$t('editor.modal_form_uploadtext'),
        cover: newEmptyFile
      },
      articleUID: '',
      toolbar: {
        openFileToolbar: {
          icon: 'bi bi-filetype-md',
          title: this.$t('editor.open'),
          action(editor) {
            document.getElementById('mdFileIptHid').click()
          }
        },
        commitToolbar: {
          icon: 'bi bi-send',
          title: this.$t('editor.commit'),
          action(editor) {
            console.log(toRaw(editor).text)
            let postData = {
              raw_md: toRaw(editor).text,
              auid: auid
            }
            let res = axios.post(server + "/api/publish", postData, {
              headers: {
                'Authorization': 'Bearer ' + localStorage.getItem('jwt')
              }
            })
          }
        },
        settingToolbar: {
          icon: 'bi bi-gear-wide-connected',
          title: this.$t('editor.setting'),
          action(editor) {
            document.getElementById('modalHideBtn').click()
          }
        }
      }
    };
  },
  methods: {
    setValid(elem) {
      elem.style = "border-color: var(--bs-success-border-subtle); color: var(--bs-success-text-emphasis);"
    },
    setNotvalid(elem) {
      elem.style = "border-color: var(--bs-danger-border-subtle); color: var(--bs-danger-text-emphasis);"
    },
    checkValid() {
      let bAllValid = true
      const title = document.getElementById('floatingTitle')
      const tags = document.getElementById('floatingTags')
      const lang = document.getElementById('selectLangOptions')
      const ipt = document.getElementById('coverIptVis')
      const iptHid = document.getElementById('coverIptHid')
      const iptBtn = document.getElementById('button-addon1')

      for (let elem of [title, tags, lang]) {
        if (elem.value) {
          this.setValid(elem)
        }
        else {
          this.setNotvalid(elem)
          bAllValid = false
        }
      }
      if (iptHid.value) {
        this.setValid(ipt)
        this.setValid(iptBtn)
      }
      else {
        this.setNotvalid(ipt)
        this.setNotvalid(iptBtn)
        bAllValid = false
      }
      return bAllValid
    },
    async getFileData() {
      // console.log(this.$refs)
      if (this.$refs.file.files[0]) {
        this.submitForm.cover = this.$refs.file.files[0];
        const res = await this.uploadImageReq([this.submitForm.cover])
        this.submitForm.cover_url = res.data.url
      }
      else {
        this.submitForm.cover = newEmptyFile
        this.submitForm.cover_url = this.$t('editor.modal_form_uploadtext')
      }
      // console.log(this.submitForm.cover)
    },
    getMarkdownLocal() {
      if (this.$refs.mdFile.files[0]) {
        let mdFile = this.$refs.mdFile.files[0]
        let mdLocal = new FileReader()
        let res = ""
				mdLocal.onload = function(e) {
					res = String(e.target.result);
				};
        mdLocal.readAsText(mdFile, "UTF-8")
        setTimeout(() => {
          this.text = res
        }, 100)
      }
    },
    uploadCover() {
      document.getElementById('coverIptHid').click()
    },
    async submitMeta() {
      if (this.checkValid()) {
        let postData = {
          auid: this.submitForm.auid,
          title: this.submitForm.title,
          cover_url: this.submitForm.cover_url,
          tags: this.submitForm.tags,
          lang: this.submitForm.lang
        }
        let res = axios.post(this.$server + "/api/savemeta", postData, {
          headers: {
            'Authorization': 'Bearer ' + localStorage.getItem('jwt')
          }
        })
      }
    },
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
      let res_img = await this.uploadImageReq(file);

      insertImage({
        url: this.$server + res_img.data.url,
        desc: file[0].name
      });
    },
    async saveArticle(text, html) {
      let postData = {
        md: text,
        auid: this.articleUID
      }
      let res = axios.post(this.$server + "/api/saveMD", postData, {
        headers: {
          'Authorization': 'Bearer ' + localStorage.getItem('jwt')
        }
      })
    },
    async getArticleUID() {
      try {
        let res = axios.get(this.$server + '/api/getUUID')
        res.then((value) => {
          this.articleUID = value.data.uuid
          auid = value.data.uuid
          this.submitForm.auid = value.data.uuid
          // console.log("Get new AUID")
        })
      }
      catch (error) {
        console.log(error)
        this.text = "Get Article Unique ID Failed, Please Refresh Page (F5).\n获取文章UID失败，请刷新页面。"
      }
    },
    async getArticle(local_auid) {
      try {
        let res = axios.get(this.$server + '/api/article/' + local_auid)
        res.then((r) => {
          let value = r.data
          // console.log(value)
          if (value.data.art_md){
            this.text = value.data.art_md;
            this.submitForm.cover_url = value.data.art_meta.cover_url;
            this.submitForm.tags = value.data.art_meta.tags;
            this.submitForm.lang = value.data.art_meta.lang;
            this.submitForm.title = value.data.art_meta.title;
            this.submitForm.auid = local_auid;
            auid = local_auid;
          }
        })
      }
      catch (error) {
        console.log(error)
        this.text = "Get Article Failed, Please Refresh Page (F5).\n获取文章失败，请刷新页面。"
      }
    }
  },
  mounted() {
    server = this.$server
    if (this.$route.query.auid) {
      this.getArticle(this.$route.query.auid)
    }
    else {
      this.getArticleUID();
    }
  }
};
</script>

<style>
html, body {
  overflow: auto !important;
}

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

.v-md-textarea-editor textarea,
.vuepress-markdown-body tr:nth-child(2n) {
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