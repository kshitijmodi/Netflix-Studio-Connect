# Design Guidelines: Modern Task Management App

## Design Approach

**System:** Linear-inspired productivity design with Notion's information hierarchy
**Rationale:** Task management demands clarity, efficiency, and visual hierarchy. Linear's clean aesthetics combined with Notion's data organization patterns create an optimal environment for focus and productivity.

**Core Principles:**
- Information clarity over decoration
- Immediate action availability
- Visual feedback for all interactions
- Spatial organization reflecting priority

## Typography

**Font Family:** Inter (Google Fonts)
- Primary: Inter (400, 500, 600)
- All text rendering with antialiasing for crispness

**Hierarchy:**
- Page Title: text-2xl, font-semibold (Task Manager, Filter labels)
- Task Title: text-base, font-medium
- Task Description: text-sm, font-normal
- Meta Information: text-xs, font-normal (dates, counts)
- Button Text: text-sm, font-medium

## Layout System

**Spacing Primitives:** Tailwind units of 2, 4, 6, and 8
- Component padding: p-4, p-6
- Gap between elements: gap-4, gap-6
- Margins: m-2, m-4, m-8
- Card spacing: space-y-4

**Container Structure:**
- Max width: max-w-6xl centered
- Main content area: 70% width on desktop
- Sidebar/filters: 30% width on desktop
- Mobile: Full-width stack

## Component Library

### Task Cards
- Rounded corners: rounded-lg
- Padding: p-4
- Border: border with subtle treatment
- Shadow on hover for depth
- Checkbox on left, content center, priority badge right
- Drag handle icon visible on hover (left edge)

### Priority Badges
- High: Bold, prominent pill shape
- Medium: Moderate pill shape
- Low: Subtle pill shape
- Size: px-3 py-1, text-xs, rounded-full

### Input Fields
- Task title input: Large, borderless on create
- Task description: text-sm, multi-line textarea
- Focused state: Subtle border highlight
- Placeholder text with reduced opacity

### Buttons & Actions
- Primary CTA: px-4 py-2, rounded-md, font-medium
- Secondary: Ghost style with hover background
- Icon buttons: p-2, rounded-md
- Delete actions: Subtle until hover

### Filters & Controls
- Pill-style filter buttons: px-4 py-2, rounded-full
- Active filter: Filled background
- Inactive: Outline or ghost style
- Horizontal layout with gap-2

### Modals/Dialogs
- Centered overlay with backdrop blur
- Card style: p-6, rounded-lg, max-w-md
- Form fields with consistent spacing (space-y-4)

## Drag-and-Drop Visual Feedback

- **Dragging state:** Reduced opacity (0.5), slight rotation (rotate-2)
- **Drop zones:** Dashed border indication when item hovers
- **Reorder preview:** Gap opens between items showing insertion point
- **Cursor:** grab cursor on drag handles, grabbing when active

## Status & Interaction States

**Completed Tasks:**
- Strikethrough text (line-through)
- Reduced opacity (opacity-60)
- Checkbox filled/checked state
- Subtle visual separation from active tasks

**Empty States:**
- Centered message with icon
- Encouraging microcopy
- CTA button to create first task

**Loading States:**
- Skeleton screens matching task card structure
- Pulsing animation on placeholders

## Responsive Behavior

**Desktop (lg):**
- Two-column layout (filters + tasks)
- Horizontal filter pills
- Expanded task cards with full descriptions

**Mobile (base):**
- Single column stack
- Compact filter dropdown/toggle
- Condensed task cards, expandable on tap
- Sticky add button (bottom-right floating)

## Animation Guidelines

**Minimal, purposeful animations only:**
- Task completion: Smooth fade + strikethrough (200ms)
- Drag and drop: Transform transitions (150ms)
- Modal open/close: Fade + scale (200ms)
- Filter switching: Fade content swap (150ms)
- NO elaborate scroll animations or unnecessary motion

## Information Architecture

**Main View Structure:**
1. Header: App title + Quick add button
2. Filter Bar: All/Active/Completed + Priority filters
3. Task List: Cards organized by priority or custom order
4. Floating Action: Add new task (bottom-right on mobile)

**Task Card Content:**
- Drag handle (subtle, left edge)
- Checkbox (left)
- Task title + description (center, vertical stack)
- Priority badge (top-right)
- Actions menu (ellipsis, top-right, visible on hover)