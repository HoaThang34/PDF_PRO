export default function Hero() {
  return (
    <section className="hero" id="hero">
      <div className="container hero-grid">
        <div className="hero-content">
          <div className="hero-badge">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" width="14" height="14">
              <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2" />
            </svg>
            Công cụ PDF số 1 Việt Nam
          </div>
          <h1 className="hero-title">
            Xử lý PDF <span className="gradient-text">Chuyên Nghiệp</span>
            <br />Nhanh - An Toàn - Miễn Phí
          </h1>
          <p className="hero-subtitle">
            PDF PRO là bộ công cụ toàn diện giúp bạn merge, split, compress, chỉnh sửa và xử lý
            mọi loại file PDF với tốc độ nhanh nhất. Hỗ trợ AI thông minh, bảo mật tuyệt đối.
          </p>
          <div className="hero-cta">
            <a href="https://github.com/HoaThang34/PDF_PRO/releases/download/v1.0.0/PDF-PRO.exe" className="btn btn-primary btn-lg">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" width="20" height="20">
                <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
                <polyline points="7 10 12 15 17 10" />
                <line x1="12" y1="15" x2="12" y2="3" />
              </svg>
              Tải xuống miễn phí
            </a>
            <a href="#tools" className="btn btn-outline btn-lg">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" width="20" height="20">
                <polygon points="5 3 19 12 5 21 5 3" />
              </svg>
              Xem công cụ
            </a>
          </div>
        </div>

        <div className="hero-visual">
          <div className="hero-mockup">
            <img
              src="/homepage.png"
              alt="PDF PRO Giao diện"
              className="mockup-screenshot"
            />
          </div>

          <div className="floating-badge b1">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" width="14" height="14">
              <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z" />
            </svg>
            Fast Export
          </div>
          <div className="floating-badge b2">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" width="14" height="14">
              <path d="M12 2a4 4 0 0 1 4 4c0 2-2 4-4 4s-4-2-4-4 1.79-4 4-4z" />
              <path d="M20 22v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" />
            </svg>
            AI PDF
          </div>
          <div className="floating-badge b3">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" width="14" height="14">
              <rect x="3" y="11" width="18" height="11" rx="2" ry="2" />
              <path d="M7 11V7a5 5 0 0 1 10 0v4" />
            </svg>
            Secure
          </div>
          <div className="floating-badge b4">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" width="14" height="14">
              <polyline points="20 6 9 17 4 12" />
            </svg>
            No Watermark
          </div>
        </div>
      </div>
    </section>
  )
}
