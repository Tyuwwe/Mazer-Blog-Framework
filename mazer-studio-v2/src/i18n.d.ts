type Translation = (path: string, option?: Record<string, any>) => import('vue').ComputedRef<string>
interface I18n {
  locale: string
  language: Record<string, any>
  t: Translation
}