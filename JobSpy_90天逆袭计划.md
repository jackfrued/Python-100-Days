# JobSpy - 招聘数据采集与分析平台

> 90天逆袭计划：从零到实习offer

---

## 📊 用户画像

| 维度 | 现状 |
|------|------|
| **基础** | Python全栈学过，能AI辅助快速实现 |
| **专业** | 集成电路（研究生） |
| **偏好** | 数据分析 > 后端开发 |
| **环境** | Windows |
| **服务器** | 零经验，需要从零开始 |
| **目标** | 中小厂实习 → 秋招冲大厂 |
| **时间** | 90天冲刺（近1-2个月找到日常实习） |

---

## 🎯 项目方向

**项目名称：** JobSpy - 招聘数据采集与分析平台

**项目亮点：**
- 爬取各大招聘网站数据（拉勾/Boss直聘/智联）
- 数据清洗 + ETL 流程
- 数据分析 + 可视化报表
- API 接口服务
- 这是一个**能展示后端能力 + 数据分析能力**的完整项目！

**技术栈：**

| 模块 | 技术选型 | 理由 |
|------|----------|------|
| **Web框架** | FastAPI | 比Django轻量、比Flask规范、面试加分 |
| **爬虫** | Scrapy / Requests | 你教程学过，容易上手 |
| **数据库** | PostgreSQL + Redis | 生产级标配，面试必问 |
| **认证** | JWT | 主流方案 |
| **任务队列** | Celery + Redis | 你教程学过，容易上手 |
| **部署** | Docker + 云服务器 | 补齐你的短板 |
| **CI/CD** | GitHub Actions | 免费、主流 |
| **可视化** | ECharts / Pyecharts | 数据分析展示 |

---

## 📅 90天计划总览

### 第一阶段：环境准备 & 项目规划（Day 1-3）
- [ ] WSL2 安装配置
- [ ] 云服务器选购
- [ ] GitHub 仓库初始化

### 第二阶段：爬虫模块开发（Day 4-15）
- [ ] 基础爬虫开发
- [ ] 反爬应对策略
- [ ] 数据存储

### 第三阶段：后端 API 开发（Day 16-35）
- [ ] FastAPI 核心功能
- [ ] 认证、缓存、权限

### 第四阶段：数据分析 & 可视化（Day 36-50）
- [ ] Pandas 数据处理
- [ ] 可视化报表
- [ ] 数据分析报告

### 第五阶段：部署上线（Day 51-65）
- [ ] Docker 容器化
- [ ] 云服务器配置
- [ ] CI/CD 自动部署

### 第六阶段：简历 & 面试（Day 66-90）
- [ ] 简历优化
- [ ] 面试高频问题准备

---

## 📁 仓库目录结构

```
jobspy-analytics/
├── backend/              # FastAPI 后端
│   ├── app/
│   │   ├── api/          # API 路由
│   │   ├── core/         # 核心配置
│   │   ├── models/       # 数据库模型
│   │   ├── schemas/      # Pydantic 模型
│   │   ├── services/    # 业务逻辑
│   │   └── main.py       # 入口文件
│   ├── tests/            # 测试
│   ├── requirements.txt
│   └── Dockerfile
├── crawler/              # 爬虫模块
│   ├── spiders/          # 爬虫
│   ├── pipelines.py      # 数据处理管道
│   └── items.py          # 数据模型
├── etl/                  # 数据处理
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── frontend/             # 前端（可选，简化版）
├── docker/               # Docker 配置
├── scripts/               # 脚本
├── docs/                  # 文档
├── .github/
│   └── workflows/        # CI/CD
├── docker-compose.yml
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 📋 每日任务表（Week 1 示例）

| Day | 上午 (2h) | 下午 (2h) | 晚上 (1h) |
|-----|----------|----------|----------|
| Day 4 | WSL 安装配置 | Python 环境确认 | 复习爬虫基础 |
| Day 5 | 学习 Scrapy 框架 | Scrapy 项目初始化 | 看教程例子 |
| Day 6 | Boss 直聘爬虫 | 数据解析 | 反爬策略 |
| Day 7 | 完善爬虫 | 代理池搭建 | 调试优化 |
| Day 8 | PostgreSQL 安装 | 数据模型设计 | SQL 练习 |
| Day 9 | 数据入库 | 增量更新 | 调试 |
| Day 10 | 周末：整体测试爬虫 | 周末：数据量统计 | 记录问题 |

---

## 🚀 开发步骤

### Step 1: 创建 GitHub 仓库

1. 访问 https://github.com 并登录
2. 点击右上角 "+" → "New repository"
3. 填写信息：
   - Repository name: `jobspy-analytics`
   - Description: `招聘数据采集与分析平台`
   - Public / Private: Public（推荐，面试官能看到）
   - 勾选 "Add a README file"
   - 勾选 "Add .gitignore" → 选择 Python
4. 点击 "Create repository"

### Step 2: 本地克隆

```bash
# 在 WSL 或 Git Bash 中执行
git clone https://github.com/你的用户名/jobspy-analytics.git
cd jobspy-analytics
```

### Step 3: 创建目录结构

```bash
mkdir -p backend/app/{api,core,models,schemas,services}
mkdir -p backend/tests
mkdir -p crawler/spiders
mkdir -p etl
mkdir -p frontend
mkdir -p docker
mkdir -p scripts
mkdir -p docs
mkdir -p .github/workflows
touch backend/app/__init__.py
touch backend/app/main.py
touch crawler/spiders/__init__.py
touch etl/__init__.py
```

### Step 4: 提交到 GitHub

```bash
git add .
git commit -m "feat: 初始化项目结构"
git push origin main
```

---

## 🔧 技术要点

### 爬虫要点

```python
# requests + fake_useragent 防反爬
import requests
from fake_useragent import UserAgent

ua = UserAgent()
headers = {'User-Agent': ua.random}

response = requests.get(url, headers=headers, timeout=10)

# PostgreSQL 存储
import psycopg2

conn = psycopg2.connect(database="jobspy", user="admin", password="xxx")
cursor.execute(
    "INSERT INTO jobs (title, company, salary, city, tags) VALUES (%s, %s, %s, %s, %s)",
    (title, company, salary, city, tags)
)
conn.commit()
```

### FastAPI 要点

```python
# FastAPI + SQLAlchemy + PostgreSQL
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

app = FastAPI()

class JobFilter(BaseModel):
    city: str | None = None
    salary_min: int | None = None
    tags: list[str] | None = None

@app.get("/jobs/")
def get_jobs(filter: JobFilter, db: Session = Depends(get_db)):
    query = db.query(Job)
    if filter.city:
        query = query.filter(Job.city == filter.city)
    return query.limit(100).all()
```

### 数据分析要点

```python
# 数据分析示例
import pandas as pd
from pyecharts import Bar, Pie, Line

# 薪资分布分析
df['salary_num'] = df['salary'].str.extract(r'(\d+)').astype(float)
salary_stats = df.groupby('city')['salary_num'].agg(['mean', 'median', 'count'])

# 生成可视化
bar = Bar("各城市平均薪资")
bar.add("平均薪资", salary_stats.index, salary_stats['mean'].values)
bar.render("salary_by_city.html")
```

---

## 📝 简历项目描述（完成后填写）

```
项目名称：JobSpy - 招聘数据采集与分析平台
技术栈：Python + FastAPI + Scrapy + PostgreSQL + Redis + Docker + ECharts

项目描述：
  针对 Python 就业市场数据进行分析，从 Boss 直聘、拉勾等平台
  采集职位信息，构建数据仓库，提供职位搜索、薪资分析、
  技能要求分析等功能。

个人职责：
  - 设计爬虫架构，实现增量更新机制
  - 构建 FastAPI RESTful API，支持数据查询和导出
  - 使用 Redis 实现热门数据缓存，响应时间降低 60%
  - 部署至云服务器，实现 CI/CD 自动发布

技术亮点：
  - 日采集数据量 5000+，存储 PostgreSQL
  - API 响应时间 < 100ms
  - Docker 容器化部署，GitHub Actions 自动构建
```

---

## ❓ 面试高频问题（针对这个项目）

### Q1: 爬虫的反爬机制怎么处理的？

回答思路：
- User-Agent 轮换
- 请求间隔随机化
- IP 代理池（可选）
- Cookies 处理
- 验证码识别（简单图片可以 OCR）

### Q2: 数据量和性能怎么保证？

回答思路：
- 分页采集 + 增量更新
- Redis 缓存热门查询
- 数据库索引优化
- 异步任务队列（Celery）

### Q3: 你这个专业为什么做 Python 后端？

回答思路（跨专业优势）：
- 研究生阶段接触数据处理，Python 是主要工具
- 集成电路设计中 EDA 工具大量使用 Python
- 对数据敏感，希望做数据驱动的开发
- 研究生培养的逻辑思维和解决问题的能力

---

## ⚠️ 注意事项

1. **服务器购买**：尽快购买腾讯云/阿里云学生机（~10元/月）
2. **时间管理**：如果某个阶段太赶，可以砍掉"前端展示"部分
3. **论文**：把论文相关的数据处理也做成这个项目的一部分，一举两得
4. **面试**：边做项目边投简历，不要等项目做完才投

---

## 📚 学习资源

### Docker 基础（必须）
- B站 "Docker 入门" 视频，2天速成

### Redis 基础（必须）
- 教程 Day56 有，复习重点部分

### FastAPI 快速上手（必须）
- 官方文档 30 分钟过一遍

### GitHub Actions（推荐）
- B站 "CI/CD 入门"

### Nginx 反向代理（推荐）
- 教程 Day60 有

---

*创建时间：2026-05-14*
*计划周期：90天*
