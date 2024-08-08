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
        <v-md-editor v-model="text" height="600px"></v-md-editor>
    </div>
    <CopyRight />
</template>

<script>
export default {
  data() {
    return {
      text: '',
    };
  },
};
</script>

<style>
.editor-container {
    max-width: 1200px;
    min-width: 400px;
    width: 75%;
    margin: auto;
    margin-top: 100px;
    margin-bottom: 100px;
}

.v-md-editor, .v-md-textarea-editor {
    background-color: var(--bs-body-bg) !important;
    color: var(--bs-primary-text) !important;
}

.vuepress-markdown-body {
    background-color: var(--bs-body-bg) !important;
    color: var(--bs-primary-text) !important;
}
</style>