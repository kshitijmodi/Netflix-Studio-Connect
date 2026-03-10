# Studio Connect

## Overview

Studio Connect is a content management and collaboration platform designed for film/TV studio operations. It enables studios to manage pitches, contracts, projects, messaging, and analytics in a unified dashboard. The application follows a full-stack TypeScript architecture with a React frontend, Express backend, and PostgreSQL database.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Framework**: React 18 with TypeScript
- **Routing**: Wouter (lightweight React router)
- **State Management**: TanStack Query (React Query) for server state
- **UI Components**: shadcn/ui component library built on Radix UI primitives
- **Styling**: Tailwind CSS with custom CSS variables for theming (supports light/dark modes)
- **Build Tool**: Vite with path aliases (@/, @shared/, @assets/)

### Backend Architecture
- **Framework**: Express.js with TypeScript
- **Server Setup**: HTTP server with Vite middleware integration for development
- **API Pattern**: RESTful routes prefixed with `/api`
- **Storage**: Abstracted storage interface (IStorage) with in-memory implementation, designed for easy database migration

### Data Layer
- **ORM**: Drizzle ORM with PostgreSQL dialect
- **Schema Location**: `shared/schema.ts` for shared type definitions
- **Validation**: Zod schemas generated from Drizzle schemas via drizzle-zod
- **Migrations**: Drizzle Kit for database migrations (output to `/migrations`)

### Legacy/Alternative Implementations
- Python Streamlit implementations exist (`app.py`, `appai.py`, `cgptmain.py`) as alternative frontend prototypes
- JSON files serve as mock data stores for pitches, contracts, messages, projects, analytics, and user data

### Design System
- Uses Inter font family with defined typography hierarchy
- Dark theme with Netflix-inspired aesthetics (defined in design_guidelines.md)
- Component patterns follow Linear/Notion-inspired productivity design principles

## External Dependencies

### Frontend Dependencies
- React with react-dom
- TanStack Query for data fetching
- Radix UI primitives (dialog, dropdown, tabs, tooltip, etc.)
- Recharts for data visualization
- embla-carousel for carousels
- react-day-picker for calendar components
- react-hook-form for form handling
- cmdk for command palette
- vaul for drawer component
- lucide-react for icons
- class-variance-authority and clsx for styling utilities

### Backend Dependencies
- Express.js for HTTP server
- Drizzle ORM with PostgreSQL driver
- Zod for runtime validation

### Development Tools
- Vite with React plugin
- TypeScript with strict mode
- PostCSS with Tailwind CSS and Autoprefixer
- Drizzle Kit for database management

### Python Dependencies (Legacy)
- Streamlit for alternative UI
- Groq for AI integration
- streamlit-option-menu for navigation

### Database
- PostgreSQL (configured via DATABASE_URL environment variable)
- Database provisioning required before running migrations