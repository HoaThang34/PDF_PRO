import { useState } from 'react'
import { IconMenu, IconClose } from '../icons.jsx'

const navLinks = [
  { label: 'Trang chủ', href: '#hero' },
  { label: 'Tính năng', href: '#features' },
  { label: 'Công cụ', href: '#tools' },
  { label: 'Liên hệ', href: '#footer' },
]

export default function Header() {
  const [open, setOpen] = useState(false)

  return (
    <header className="header">
      <div className="container header-inner">
        <a href="#hero" className="logo">
          <img src="/logo.png" alt="PDF PRO" className="logo-img" />
          <span className="logo-text">PDF PRO</span>
        </a>

        <nav className={`nav ${open ? 'nav--open' : ''}`}>
          {navLinks.map((l) => (
            <a key={l.label} href={l.href} className="nav-link" onClick={() => setOpen(false)}>
              {l.label}
            </a>
          ))}
          <div className="nav-mobile-actions">
            <a href="#footer" className="btn btn-primary" onClick={() => setOpen(false)}>Tải app</a>
          </div>
        </nav>

        <div className="header-actions">
          <a href="https://github.com/HoaThang34/PDF_PRO/releases/download/v1.0.0/PDF-PRO.exe" className="btn btn-primary">
            <span className="btn-svg"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" width="16" height="16"><polyline points="21 15 21 19 3 19 3 15" /><polyline points="7 10 12 15 17 10" /><line x1="12" y1="15" x2="12" y2="3" /></svg></span>
            Tải app
          </a>
        </div>

        <button className="hamburger" onClick={() => setOpen(!open)} aria-label="Menu">
          {open ? <IconClose /> : <IconMenu />}
        </button>
      </div>
    </header>
  )
}
