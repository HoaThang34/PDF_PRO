export default function DemoSection() {
  return (
    <section className="demo-section" id="demo">
      <div className="container">
        <div className="section-header">
          <h2>Trải nghiệm trực tiếp</h2>
          <p>Xem PDF PRO hoạt động như thế nào qua video demo và hình ảnh trực quan</p>
        </div>

        <div className="demo-video">
          <div className="video-placeholder">
            <div className="video-play-btn">▶</div>
            <p>Xem video hướng dẫn</p>
          </div>
        </div>

        <div className="demo-before-after">
          <div className="ba-card ba-before">
            <div className="ba-label">Trước khi xử lý</div>
            <div className="ba-preview">
              <div className="mockup-line w60" /><div className="mockup-line w40" />
              <div className="mockup-line w70" /><div className="mockup-line w30" />
              <div style={{ height: 4, width: '100%', background: '#ef4444', borderRadius: 4, margin: '12px 0' }} />
              <div className="mockup-line w50" /><div className="mockup-line w80" />
            </div>
          </div>
          <div className="ba-arrow">→</div>
          <div className="ba-card ba-after">
            <div className="ba-label">Sau khi xử lý</div>
            <div className="ba-preview">
              <div className="mockup-line w80" /><div className="mockup-line w75" />
              <div className="mockup-line w85" /><div className="mockup-line w90" />
              <div className="mockup-line w70" /><div className="mockup-line w95" />
            </div>
          </div>
        </div>

        <div className="demo-upload">
          <div className="upload-area">
            <div className="upload-icon">📤</div>
            <p>Kéo và thả file PDF vào đây</p>
            <span className="upload-hint">Hoặc click để chọn file</span>
          </div>
        </div>
      </div>
    </section>
  )
}
