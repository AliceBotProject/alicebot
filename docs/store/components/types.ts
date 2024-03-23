export interface PyPIData {
  info: {
    author: string
    author_email: string
    classifiers: string[]
    description: string
    description_content_type: string
    docs_url: null
    download_url: string
    home_page: string
    keywords: string
    license: string
    maintainer: string
    maintainer_email: string
    name: string
    package_url: string
    platform: null
    project_url: string
    project_urls: { [key: string]: string }
    release_url: string
    requires_dist: string[]
    requires_python: string
    summary: string
    version: string
    yanked: boolean
    yanked_reason: null
  }
  last_serial: number
}

export interface PluginAdapterData {
  name: string
  time: number
  is_official: boolean
  pypi_name: string
  module_name: string
}

export interface BotData {
  name: string
  time: number
  is_official: boolean
  description: string
  author: string
  homepage: string
  tags: string
}

export type MetaData = PluginAdapterData | BotData
