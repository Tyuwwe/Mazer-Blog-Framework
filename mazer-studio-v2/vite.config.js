import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { prismjsPlugin } from 'vite-plugin-prismjs'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    prismjsPlugin({
      languages: 'all',
      plugins: ['line-numbers','show-language','copy-to-clipboard','inline-color'],
      theme: 'Twilight',
      css: true,
    })
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    proxy: {
      '/api': { // 获取请求中带 /api 的请求
        target: 'http://localhost:5000',  // 后台服务器的源
        changeOrigin: true,   // 修改源
        rewrite: (path) => path.replace(/^\/api/, "")   //  /api 替换为空字符串
      }
    }
  }
})
