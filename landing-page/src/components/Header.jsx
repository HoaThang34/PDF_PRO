import { useState } from 'react'

const navLinks = [
  { label: 'Trang chủ', href: '#hero' },
  { label: 'Tính năng', href: '#features' },
  { label: 'Công cụ', href: '#tools' },
  { label: 'Bảng giá', href: '#pricing' },
  { label: 'FAQ', href: '#faq' },
  { label: 'Liên hệ', href: '#footer' },
]

export default function Header() {
  const [open, setOpen] = useState(false)

  return (
    <header className="header">
      <div className="container header-inner">
        <a href="#hero" className="logo">
          <div className="logo-icon">P</div>
          <span className="logo-text">PDF PRO</span>
        </a>

        <nav className={`nav ${open ? 'nav--open' : ''}`}>
          {navLinks.map((l) => (
            <a key={l.label} href={l.href} className="nav-link" onClick={() => setOpen(false)}>
              {l.label}
            </a>
          ))}
        </nav>

        <div className="header-actions">
          <a href="#pricing" className="btn btn-outline">Dùng thử miễn phí</a>
          <a href="#download" className="btn btn-primary">Tải app</a>
        </div>

        <button className="hamburger" onClick={() => setOpen(!open)} aria-label="Menu">
          <span /><span /><span />
        </button>
      </div>
    </header>
  )
}
