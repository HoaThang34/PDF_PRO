export default function Hero() {
  return (
    <section className="hero" id="hero">
      <div className="container hero-grid">
        <div className="hero-content">
          <div className="hero-badge">Công cụ PDF số 1 Việt Nam</div>
          <h1 className="hero-title">
            Xử lý PDF <span className="gradient-text">Chuyên Nghiệp</span>
            <br />Nhanh - An Toàn - Miễn Phí
          </h1>
          <p className="hero-subtitle">
            PDF PRO là bộ công cụ toàn diện giúp bạn merge, split, compress, chỉnh sửa và xử lý
            mọi loại file PDF với tốc độ nhanh nhất. Hỗ trợ AI thông minh, bảo mật tuyệt đối.
          </p>
          <div className="hero-cta">
            <a href="#pricing" className="btn btn-primary btn-lg">Bắt đầu miễn phí</a>
            <a href="#demo" className="btn btn-outline btn-lg">Xem hướng dẫn</a>
          </div>
          <div className="hero-stats">
            <div className="hero-stat">
              <span className="hero-stat-num">50K+</span>
              <span className="hero-stat-label">Người dùng</span>
            </div>
            <div className="hero-stat">
              <span className="hero-stat-num">1M+</span>
              <span className="hero-stat-label">File đã xử lý</span>
            </div>
            <div className="hero-stat">
              <span className="hero-stat-num">4.9</span>
              <span className="hero-stat-label">Đánh giá</span>
            </div>
          </div>
        </div>

        <div className="hero-visual">
          <div className="hero-mockup">
            <div className="mockup-header">
              <span className="mockup-dot" /><span className="mockup-dot" /><span className="mockup-dot" />
            </div>
            <div className="mockup-body">
              <div className="mockup-sidebar">
                <div className="mockup-menu-item active" />
                <div className="mockup-menu-item" />
                <div className="mockup-menu-item" />
                <div className="mockup-menu-item" />
              </div>
              <div className="mockup-main">
                <div className="mockup-toolbar" />
                <div className="mockup-content">
                  <div className="mockup-pdf">
                    <div className="mockup-line w80" /><div className="mockup-line w60" />
                    <div className="mockup-line w70" /><div className="mockup-line w50" />
                    <div className="mockup-line w90" /><div className="mockup-line w40" />
                  </div>
                  <div className="mockup-pdf">
                    <div className="mockup-line w75" /><div className="mockup-line w65" />
                    <div className="mockup-line w55" /><div className="mockup-line w85" />
                    <div className="mockup-line w45" /><div className="mockup-line w60" />
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div className="floating-badge b1">Fast Export</div>
          <div className="floating-badge b2">AI PDF</div>
          <div className="floating-badge b3">Secure</div>
          <div className="floating-badge b4">No Watermark</div>
        </div>
      </div>
    </section>
  )
}
